from flask import jsonify, request

from app.web.general import transform_errors
from . import web
from app.models.admin_teacher import TeacherListReader, TeacherUpdater, TeacherInserter, TeacherDeleter
from app.validate.admin_teacher import AdminSelectSingleTeacherForm, AdminUpdateTeacherForm, AdminInsertTeacherForm
from app.models.teacher import TeacherReader


@web.route('/admin/teacher/select', methods=['GET'])
def admin_select_teacher():
    teacher_list_reader = TeacherListReader()
    return jsonify(teacher_list_reader.data), 404 if teacher_list_reader.data.get('error') else 200
    pass


@web.route('/admin/teacher/update', methods=['GET', 'POST'])
def admin_update_teacher():
    if request.method == 'GET':
        form = AdminSelectSingleTeacherForm(request.args)
        if form.validate():
            teacher_id = form.teacher_id.data
            teacher = TeacherReader(teacher_id)
            return jsonify(teacher.data), 404 if teacher.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    else:
        form = AdminUpdateTeacherForm(request.args)
        if form.validate():
            teacher_id = form.teacher_id.data
            teacher_name = form.teacher_name.data
            sex = form.sex.data
            birth_year = form.birth_year.data
            updater = TeacherUpdater(teacher_id, teacher_name, sex, birth_year)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
        pass


@web.route('/admin/teacher/insert', methods=['POST'])
def admin_insert_teacher():
    form = AdminInsertTeacherForm(request.args)
    if form.validate():
        teacher_name = form.teacher_name.data
        sex = form.sex.data
        birth_year = form.birth_year.data
        inserter = TeacherInserter(teacher_name, sex, birth_year)
        return jsonify(inserter.data), 404 if inserter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/teacher/delete', methods=['POST'])
def admin_delete_teacher():
    form = AdminSelectSingleTeacherForm(request.args)
    if form.validate():
        teacher_id = form.teacher_id.data
        deleter = TeacherDeleter(teacher_id)
        return jsonify(deleter.data), 404 if deleter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404

