from . import web


@web.route('/admin/student/select', methods=['GET'])
def admin_select_student():
    pass


@web.route('/admin/student/update', methods=['GET', 'POST'])
def admin_update_student():
    pass


@web.route('/admin/student/insert', methods=['GET', 'POST'])
def admin_insert_student():
    pass


@web.route('/admin/student/delete', methods=['POST'])
def admin_delete_student():
    pass
