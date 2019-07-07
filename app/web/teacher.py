from . import web
from flask import request
from flask import jsonify
from app.validate.teacher import GetTeacherInformationForm, GetCourseInformationForm, PostGradeInformationForm
from app.models.teacher import TeacherReader, TeacherCoursesReader, TeacherCourseStudentReader, TeacherGradeUpdater, \
    CourseStatisticReader
from app.web.general import transform_errors


@web.route('/teacher/information')
def get_teacher_information():
    # 查看老师基本信息
    form = GetTeacherInformationForm(request.args)
    if form.validate():
        teacher_id = form.teacher_id.data
        teacher = TeacherReader(teacher_id)
        return jsonify(teacher.data), 404 if teacher.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/courses_taught')
def get_teacher_courses_taught():
    # 查看教师授课信息
    form = GetTeacherInformationForm(request.args)
    if form.validate():
        teacher_id = form.teacher_id.data
        teacher_courses = TeacherCoursesReader(teacher_id)
        return jsonify(teacher_courses.data), 404 if teacher_courses.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/course_information', methods=['GET', 'POST'])
def get_teacher_course_information():
    if request.method == 'GET':
        # 查看某课程选课学生信息
        form = GetCourseInformationForm(request.args)
        if form.validate():
            course_id = form.course_id.data
            course_students = TeacherCourseStudentReader(course_id)
            return jsonify(course_students.data), 404 if course_students.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    else:
        # 修改某课程某学生成绩
        form = PostGradeInformationForm(request.args)
        if form.validate():
            course_id = form.course_id.data
            student_id = form.student_id.data
            grade = form.grade.data
            grade_updater = TeacherGradeUpdater(course_id, student_id, grade)
            return jsonify(grade_updater.data), 404 if grade_updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/course_statistic')
def get_teacher_course_statistic():
    form = GetCourseInformationForm(request.args)
    if form.validate():
        course_id = form.course_id.data
        course_students = CourseStatisticReader(course_id)
        return jsonify(course_students.data), 404 if course_students.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
