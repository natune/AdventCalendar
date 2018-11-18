from flask import Flask

from app.views.login_view import login_page


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')

    app.register_blueprint(login_page)

    return app
