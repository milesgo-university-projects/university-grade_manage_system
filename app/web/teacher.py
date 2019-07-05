from . import web
from flask import request
from flask import jsonify
from app.validate.teacher import GetTeacherInformationForm, GetCourseInformationForm


@web.route('/teacher/information')
def get_teacher_information():
    form = GetTeacherInformationForm(request.args)
    if form.validate():
        teacher_id = form.student_id.data
        return 'get teacher information, teacher id is ' + teacher_id
    else:
        return jsonify(form.errors)
    pass


@web.route('/teacher/courses_taught')
def get_teacher_courses_taught():
    form = GetTeacherInformationForm(request.args)
    if form.validate():
        teacher_id = form.teacher_id.data
        return 'get teacher information, teacher id is ' + teacher_id
    else:
        return jsonify(form.errors)
    pass


@web.route('/teacher/course_information')
def get_teacher_course_information():
    form = GetCourseInformationForm(request.args)
    if form.validate():
        course_id = form.course_id.data
        return 'get course information, course id is ' + course_id
    else:
        return jsonify(form.errors)
    pass


@web.route('/teacher/course_statistic')
def get_teacher_course_statistic():
    pass
