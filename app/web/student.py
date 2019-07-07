from . import web
from flask import request
from flask import jsonify
from app.validate.student import GetStudentInformationForm
from app.models.student import StudentReader, StudentCoursesReader
from app.web.general import transform_errors
from flask_login import login_required
from app.validate.general import check_authority


@web.route('/student/information')
@login_required
def get_student_information():
    form = GetStudentInformationForm(request.args)  # 验证请求参数
    if form.validate():  # 如果通过验证
        student_id = form.student_id.data
        authority = check_authority('student', student_id)
        if authority.get('error'):
            return jsonify(authority), 404
        student = StudentReader(student_id)  # 从数据库读取学生信息
        # 若包含error字段，则读取失败，否则读取成功
        return jsonify(student.data), 404 if student.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/student/courses_selected')
@login_required
def get_student_courses_selected():
    form = GetStudentInformationForm(request.args)
    if form.validate():
        student_id = form.student_id.data
        authority = check_authority('student', student_id)
        if authority.get('error'):
            return jsonify(authority), 404
        student_courses = StudentCoursesReader(student_id)
        return jsonify(student_courses.data), 404 if student_courses.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404
