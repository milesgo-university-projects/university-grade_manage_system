from werkzeug.utils import redirect
from app import create_app
from flask_login import login_required


app = create_app()


@app.route('/')
def bare():
    return redirect('/static/Login.html')


@app.route('/static/Login.html')
def html_login():
    return app.send_static_file('Login.html')


@app.route('/static/Student_Info.html')
@login_required
def html_student_info():
    return app.send_static_file('Student_Info.html')


@app.route('/static/Student_Scores.html')
@login_required
def html_student_scores():
    return app.send_static_file('Student_Scores.html')


@app.route('/static/Student_ChangePassword.html')
@login_required
def html_student_change_password():
    return app.send_static_file('Student_ChangePassword.html')


@app.route('/static/Teacher_Info.html')
@login_required
def html_teacher_info():
    return app.send_static_file('Teacher_Info.html')


@app.route('/static/Teacher_Courses.html')
@login_required
def html_teacher_courses():
    return app.send_static_file('Teacher_Courses.html')


@app.route('/static/Teacher_CourseInfo.html')
@login_required
def html_course_info():
    return app.send_static_file('Teacher_CourseInfo.html')


@app.route('/static/Teacher_ChangePassword.html')
@login_required
def html_teacher_change_password():
    return app.send_static_file('Teacher_ChangePassword.html')


@app.route('/static/Teacher_Statistics.html')
@login_required
def html_teacher_statistics():
    return app.send_static_file('Teacher_Statistics.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)
