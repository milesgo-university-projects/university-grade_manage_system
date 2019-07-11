from flask import request, jsonify
from flask_login import login_required
from app.validate.general import check_authority
from app.web.general import transform_errors
from . import web
from app.validate.admin_course import AdminSelectSingleCourseForm, AdminInsertCourseForm, AdminUpdateCourseForm
from app.models.admin_course import CourseDeleter, CourseInserter, SingleCourseReader, CourseUpdater, CourseReader
from app.models.admin_teacher import TeacherIdReader, TeacherListReader


@web.route('/admin/course/select', methods=['GET'])
@login_required
def admin_select_course():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    course_list = CourseReader()
    return jsonify(course_list.data), 404 if course_list.data.get('error') else 200


@web.route('/admin/course/update', methods=['GET', 'POST'])
@login_required
def admin_update_course():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    if request.method == 'GET':
        form = AdminSelectSingleCourseForm(request.args)
        if form.validate():
            course_id = form.course_id.data
            result = SingleCourseReader(course_id).data
            if result.get('error'):
                return jsonify(result), 404
            result = dict(result, **TeacherListReader().data)
            return jsonify(result), 404 if result.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    else:
        form = AdminUpdateCourseForm(request.args)
        if form.validate():
            course_id = form.course_id.data
            course_name = form.course_name.data
            year = form.year.data
            semester = form.semester.data
            teacher_id = form.teacher_id.data
            credit = form.credit.data
            updater = CourseUpdater(course_id, course_name, year, semester, teacher_id, credit)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/course/insert', methods=['GET', 'POST'])
@login_required
def admin_insert_course():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    if request.method == 'GET':
        teachers = TeacherListReader()  # 获取可供选择的id列表
        return jsonify(teachers.data), 404 if teachers.data.get('error') else 200
    else:
        form = AdminInsertCourseForm(request.args)
        if form.validate():
            course_name = form.course_name.data
            year = form.year.data
            semester = form.semester.data
            teacher_id = form.teacher_id.data
            credit = form.credit.data
            inserter = CourseInserter(course_name, year, semester, teacher_id, credit)
            return jsonify(inserter.data), 404 if inserter.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/course/delete', methods=['POST'])
@login_required
def admin_delete_course():
    authority = check_authority('admin', 'default')
    if authority.get('error'):
        return jsonify(authority), 404
    form = AdminSelectSingleCourseForm(request.args)
    if form.validate():
        course_id = form.course_id.data
        deleter = CourseDeleter(course_id)
        return jsonify(deleter.data), 404 if deleter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
