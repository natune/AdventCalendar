"""アプリケーションの作成や設定の反映などを行うモジュール"""
from flask import Flask

from app import migrate, models, resources, views
from app.models import db


def create_app():
    """アプリケーションオブジェクトの作成を行う

    Returns:
        flask.app.Flask: 初期設定を行ったアプリケーションのオブジェクト
    """
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')
    models.init_app(app)
    views.init_app(app)
    migrate.init_app(app, db)
    resources.init_app(app)
    return app
