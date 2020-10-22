from flask import Flask
from flask_login import LoginManager
from app.models.session import LoginChecker
from werkzeug.utils import redirect
from flask_login import login_required

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    if 'student' in user_id:
        return LoginChecker('load', 'student', user_id[7:], 'default')
    if 'teacher' in user_id:
        return LoginChecker('load', 'teacher', user_id[7:], 'default')
    if 'admin' in user_id:
        return LoginChecker('load', 'admin', user_id[5:], 'default')
    return None


app = Flask(__name__)
login_manager.init_app(app)
from app.web.student import web
app.register_blueprint(web)


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
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '123456'
    app.config['DATABASE_USER'] = 'root'
    app.config['DATABASE_PASSWORD'] = 'asdfg13579'
    app.run(host='0.0.0.0', port=6060)
