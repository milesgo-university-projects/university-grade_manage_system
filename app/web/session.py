from flask import request, jsonify, redirect

from app.validate.general import check_authority
from app.web.general import transform_errors
from . import web
from app.validate.session import StudentChangePasswordForm, TeacherChangePasswordForm, StudentLoginForm, \
    TeacherLoginForm, AdminLoginForm
from app.models.session import StudentPasswordChanger, TeacherPasswordChanger, LoginChecker
from flask_login import login_user, login_required, logout_user


# @web.route('/')
# def bare():
#    return redirect('/static/Login.html')


@web.route('/student/login', methods=['GET'])
def student_login():
    form = StudentLoginForm(request.args)
    if form.validate():
        student_id = form.student_id.data
        password = form.password.data
        checker = LoginChecker('login', 'student', student_id, password)
        if checker.data.get('error'):
            return jsonify(checker.data), 404
        login_user(checker)
        return jsonify(checker.data), 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/student/change_password', methods=['POST'])
@login_required
def student_change_password():
    form = StudentChangePasswordForm(request.args)
    if form.validate():  # 如果通过验证
        student_id = form.student_id.data
        authority = check_authority('student', student_id)
        if authority.get('error'):
            return jsonify(authority), 404
        old_password = form.old_password.data
        new_password = form.new_password.data
        student = StudentPasswordChanger(student_id, old_password, new_password)
        return jsonify(student.data), 404 if student.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/login', methods=['GET'])
def teacher_login():
    form = TeacherLoginForm(request.args)
    if form.validate():
        teacher_id = form.teacher_id.data
        password = form.password.data
        checker = LoginChecker('login', 'teacher', teacher_id, password)
        if checker.data.get('error'):
            return jsonify(checker.data), 404
        login_user(checker)
        return jsonify(checker.data), 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/teacher/change_password', methods=['POST'])
@login_required
def teacher_change_password():
    form = TeacherChangePasswordForm(request.args)
    if form.validate():  # 如果通过验证
        teacher_id = form.teacher_id.data
        authority = check_authority('teacher', teacher_id)
        if authority.get('error'):
            return jsonify(authority), 404
        old_password = form.old_password.data
        new_password = form.new_password.data
        teacher = TeacherPasswordChanger(teacher_id, old_password, new_password)
        return jsonify(teacher.data), 404 if teacher.data.get('error') else 200
    else:  # 如果未通过验证
        return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/login', methods=['GET'])
def admin_login():
    form = AdminLoginForm(request.args)
    if form.validate():
        password = form.password.data
        checker = LoginChecker('login', 'admin', 'admin', password)
        if checker.data.get('error'):
            return jsonify(checker.data), 404
        login_user(checker)
        return jsonify(checker.data), 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/student/logout', methods=['GET'])
@login_required
def student_logout():
    logout_user()
    return '{}', 200


@web.route('/teacher/logout', methods=['GET'])
@login_required
def teacher_logout():
    logout_user()
    return '{}', 200


@web.route('/admin/logout', methods=['GET'])
@login_required
def admin_logout():
    logout_user()
    return '{}', 200
