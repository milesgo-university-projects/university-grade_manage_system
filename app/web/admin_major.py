from flask import jsonify, request

from app.web.general import transform_errors
from . import web
from app.models.admin_major import MajorReader, SingleMajorReader, MajorUpdater, MajorInserter, MajorDeleter
from app.validate.admin_major import AdminSelectSingleMajorForm, AdminUpdateMajorForm, AdminInsertMajorForm


@web.route('/admin/major/select', methods=['GET'])
def admin_select_major():
    major_reader = MajorReader()
    return jsonify(major_reader.data), 404 if major_reader.data.get('error') else 200
    pass


@web.route('/admin/major/update', methods=['GET', 'POST'])
def admin_update_major():
    if request.method == 'GET':
        form = AdminSelectSingleMajorForm(request.args)
        if form.validate():
            major_id = form.major_id.data
            major = SingleMajorReader(major_id)
            return jsonify(major.data), 404 if major.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404
    else:
        form = AdminUpdateMajorForm(request.args)
        if form.validate():
            major_id = form.major_id.data
            major_name = form.major_name.data
            updater = MajorUpdater(major_id, major_name)
            return jsonify(updater.data), 404 if updater.data.get('error') else 200
        else:
            return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/major/insert', methods=['POST'])
def admin_insert_major():
    form = AdminInsertMajorForm(request.args)
    if form.validate():
        major_name = form.major_name.data
        inserter = MajorInserter(major_name)
        return jsonify(inserter.data), 404 if inserter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404


@web.route('/admin/major/delete', methods=['POST'])
def admin_delete_major():
    form = AdminSelectSingleMajorForm(request.args)
    if form.validate():
        major_id = form.major_id.data
        deleter = MajorDeleter(major_id)
        return jsonify(deleter.data), 404 if deleter.data.get('error') else 200
    else:
        return jsonify(transform_errors(form.errors)), 404

