from flask import jsonify, request
from flask_login import login_required

from app.validate.general import check_authority
from . import web
from app.models.admin_student import StudentListReader, StudentUpdater, StudentInserter, StudentDeleter
from app.validate.student import GetStudentInformationForm
from app.models.student import StudentReader
from app.web.general import transform_errors
from app.models.admin_major import MajorReader
from app.validate.admin_student import UpdateStudentInformationForm, InsertStudentInformationForm


@web.route('/admin/student/select', methods=['GET'])
@login_required
def admin_select_student():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    student_list = StudentListReader()
    return jsonify(student_list.data), 404 if student_list.data.get('error') else 200


@web.route('/admin/student/update', methods=['GET', 'POST'])
@login_required
def admin_update_student():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    if request.method == 'GET':
        form = GetStudentInformationForm(request.args)
        if form.validate():
            student_id = form.student_id.data
            student = StudentReader(student_id)
            result = student.data  # 获取学生基本信息
            majors = MajorReader()  # 获取可供选择的id列表
            result = dict(result, **majors.data)
            return jsonify(result), 404 if result.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    else:
        form = UpdateStudentInformationForm(request.args)
        if form.validate():
            student_id = form.student_id.data
            student_name = form.student_name.data
            sex = form.sex.data
            birth_year = form.birth_year.data
            province = form.province.data
            enter_year = form.enter_year.data
            major_id = form.major_id.data
            updater = StudentUpdater(student_id, student_name, sex, birth_year, province, enter_year, major_id)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/student/insert', methods=['GET', 'POST'])
@login_required
def admin_insert_student():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    if request.method == 'GET':
        majors = MajorReader()  # 获取可供选择的id列表
        return jsonify(majors.data), 404 if majors.data.get('error') else 200
    else:
        form = InsertStudentInformationForm(request.args)
        if form.validate():
            student_name = form.student_name.data
            sex = form.sex.data
            birth_year = form.birth_year.data
            province = form.province.data
            enter_year = form.enter_year.data
            major_id = form.major_id.data
            inserter = StudentInserter(student_name, sex, birth_year, province, enter_year, major_id)
            return jsonify(inserter.data), 404 if inserter.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/student/delete', methods=['POST'])
@login_required
def admin_delete_student():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    form = GetStudentInformationForm(request.args)
    if form.validate():
        student_id = form.student_id.data
        deleter = StudentDeleter(student_id)
        return jsonify(deleter.data), 404 if deleter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
