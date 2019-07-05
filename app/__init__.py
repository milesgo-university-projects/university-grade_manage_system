from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.normal_config')  # 载入配置文件
    app.config.from_object('app.secure_config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.student import web
    app.register_blueprint(web)
