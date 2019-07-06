from . import web


@web.route('/admin/course/select', methods=['GET'])
def admin_select_course():
    pass


@web.route('/admin/course/update', methods=['GET', 'POST'])
def admin_update_course():
    pass


@web.route('/admin/course/insert', methods=['GET', 'POST'])
def admin_insert_course():
    pass


@web.route('/admin/course/delete', methods=['POST'])
def admin_delete_course():
    pass
