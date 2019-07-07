from flask import Flask
from flask_login import LoginManager
from app.models.session import LoginChecker

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    if 'student' in user_id:
        return LoginChecker('load', 'student', user_id[7:], 'default')
    return None


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.normal_config')  # 载入配置文件
    app.config.from_object('app.secure_config')
    register_blueprint(app)
    login_manager.init_app(app)
    return app


def register_blueprint(app):
    from app.web.student import web
    app.register_blueprint(web)
