from app.web.general import transform_errors
from . import web
from app.models.admin_major_course import MajorCourseReader, InsertMajorCourseReader, MajorCourseInserter, MajorCourseDeleter
from app.validate.admin_major_course import AdminMajorCourseForm
from flask import request, jsonify


@web.route('/admin/major_course/select', methods=['GET'])
def admin_select_major_course():
    # 没有参数，不需要验证
    major_courses = MajorCourseReader()
    return jsonify(major_courses.data), 404 if major_courses.data.get('error') else 200


@web.route('/admin/major_course/insert', methods=['GET', 'POST'])
def admin_insert_major_course():
    if request.method == 'GET':
        insert_major_courses = InsertMajorCourseReader()
        return jsonify(insert_major_courses.data), 404 if insert_major_courses.data.get('error') else 200
    else:
        form = AdminMajorCourseForm(request.args)
        if form.validate():
            major_id = form.major_id.data
            course_id = form.course_id.data
            insert_major_courses = MajorCourseInserter(major_id, course_id)
            return jsonify(insert_major_courses.data), 404 if insert_major_courses.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/major_course/delete', methods=['POST'])
def admin_delete_major_course():
    form = AdminMajorCourseForm(request.args)
    if form.validate():
        major_id = form.major_id.data
        course_id = form.course_id.data
        delete_major_courses = MajorCourseDeleter(major_id, course_id)
        return jsonify(delete_major_courses.data), 404 if delete_major_courses.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404


