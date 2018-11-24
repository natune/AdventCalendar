"""アプリケーションで使用するModel層に関するモジュール"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """アプリケーションでDBを使用するための初期設定

    Args:
        app (flask.app.Flask): DBを使用するアプリケーションのオブジェクト
    """
    db.init_app(app)


class LoginUser(db.Model):
    """アプリケーションにログインするユーザ

    Attributes:
        login_id: ログインに使用するID
        password: ログインに使用するパスワードをハッシュ化した情報
    """
    login_id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
