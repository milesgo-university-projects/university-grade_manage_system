from flask import request, jsonify

from app.web.general import transform_errors
from . import web
from app.validate.session import StudentChangePasswordForm, TeacherChangePasswordForm
from app.models.session import StudentPasswordChanger, TeacherPasswordChanger


@web.route('/student/login', methods=['GET'])
def student_login():
    pass


@web.route('/student/change_password', methods=['POST'])
def student_change_password():
    form = StudentChangePasswordForm(request.args)
    if form.validate():  # 如果通过验证
        student_id = form.student_id.data
        old_password = form.old_password.data
        new_password = form.new_password.data
        student = StudentPasswordChanger(student_id, old_password, new_password)
        return jsonify(student.data), 404 if student.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/login', methods=['GET'])
def teacher_login():
    pass


@web.route('/teacher/change_password', methods=['POST'])
def teacher_change_password():
    form = TeacherChangePasswordForm(request.args)
    if form.validate():  # 如果通过验证
        teacher_id = form.teacher_id.data
        old_password = form.old_password.data
        new_password = form.new_password.data
        teacher = TeacherPasswordChanger(teacher_id, old_password, new_password)
        return jsonify(teacher.data), 404 if teacher.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/login', methods=['GET'])
def admin_login():
    pass
