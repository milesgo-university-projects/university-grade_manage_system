from flask import jsonify, request
from . import web
from app.models.admin_student import StudentListReader, StudentUpdater, StudentInserter
from app.validate.student import GetStudentInformationForm
from app.models.student import StudentReader
from app.web.general import transform_errors
from app.models.admin_major import MajorIdReader
from app.validate.admin_student import UpdateStudentInformationForm, InsertStudentInformationForm


@web.route('/admin/student/select', methods=['GET'])
def admin_select_student():
    student_list = StudentListReader()
    return jsonify(student_list.data), 404 if student_list.data.get('error') else 200


@web.route('/admin/student/update', methods=['GET', 'POST'])
def admin_update_student():
    if request.method == 'GET':
        form = GetStudentInformationForm(request.args)
        if form.validate():
            student_id = form.student_id.data
            student = StudentReader(student_id)
            result = student.data  # 获取学生基本信息
            major_id = MajorIdReader()  # 获取可供选择的id列表
            result = dict(result, **major_id.data)
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
            major_id = form.major_id.data
            updater = StudentUpdater(student_id, student_name, sex, birth_year, province, major_id)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/student/insert', methods=['GET', 'POST'])
def admin_insert_student():
    if request.method == 'GET':
        major_id = MajorIdReader()  # 获取可供选择的id列表
        return jsonify(major_id.data), 404 if major_id.data.get('error') else 200
    else:
        form = InsertStudentInformationForm(request.args)
        if form.validate():
            student_name = form.student_name.data
            sex = form.sex.data
            birth_year = form.birth_year.data
            province = form.province.data
            enter_year = form.enter_year.data
            major_id = form.major_id.data
            updater = StudentInserter(student_name, sex, birth_year, province, enter_year, major_id)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    pass


@web.route('/admin/student/delete', methods=['POST'])
def admin_delete_student():
    
    pass
