from flask import request, jsonify

from app.web.general import transform_errors
from . import web
from app.validate.admin_course import AdminSelectSingleCourseForm, AdminInsertCourseForm, AdminUpdateCourseForm
from app.models.admin_course import CourseDeleter, CourseInserter, SingleCourseReader, CourseUpdater, CourseReader
from app.models.admin_teacher import TeacherIdReader


@web.route('/admin/course/select', methods=['GET'])
def admin_select_course():
    course_list = CourseReader()
    return jsonify(course_list.data), 404 if course_list.data.get('error') else 200


@web.route('/admin/course/update', methods=['GET', 'POST'])
def admin_update_course():
    if request.method == 'GET':
        form = AdminSelectSingleCourseForm(request.args)
        if form.validate():
            course_id = form.course_id.data
            result = SingleCourseReader(course_id).data
            if result.get('error'):
                return jsonify(result), 404
            result = dict(result, **TeacherIdReader().data)
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
def admin_insert_course():
    if request.method == 'GET':
        teacher_id = TeacherIdReader()  # 获取可供选择的id列表
        return jsonify(teacher_id.data), 404 if teacher_id.data.get('error') else 200
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
def admin_delete_course():
    form = AdminSelectSingleCourseForm(request.args)
    if form.validate():
        course_id = form.course_id.data
        deleter = CourseDeleter(course_id)
        return jsonify(deleter.data), 404 if deleter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
