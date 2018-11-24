"""DBマイグレートに関するモジュール"""
from flask_migrate import Migrate


def init_app(app, db):
    """マイグレーションの適応を行う

    Args:
        app (flask.app.Flask): マイグレーションに適応させるアプリケーションのオブジェクト
        db (flask_sqlalchemy.SQLAlchemy): マイグレーション対応のModelを管理するオブジェクト
    """
    Migrate(app, db)
