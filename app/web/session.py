from . import web


@web.route('/student/login')
def student_login():
    pass


@web.route('/student/change_password')
def student_change_password():
    pass


@web.route('/teacher/login')
def teacher_login():
    pass


@web.route('/teacher/change_password')
def teacher_change_password():
    pass


@web.route('/admin/login')
def admin_login():
    pass
