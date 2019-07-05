from . import web
from flask import request
from flask import jsonify
from app.validate.student import GetStudentInformationForm
from app.models.student import StudentReader, StudentCoursesReader
from app.web.general import transform_errors


@web.route('/student/information')
def get_student_information():
    form = GetStudentInformationForm(request.args)  # 验证请求参数
    if form.validate():  # 如果通过验证
        student_id = form.student_id.data
        student = StudentReader(student_id)  # 从数据库读取学生信息
        # 若包含error字段，则读取失败，否则读取成功
        return jsonify(student.data), 404 if student.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/student/courses_selected')
def get_student_courses_selected():
    form = GetStudentInformationForm(request.args)
    if form.validate():
        student_id = form.student_id.data
        student_courses = StudentCoursesReader(student_id)
        return jsonify(student_courses.data), 404 if student_courses.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
