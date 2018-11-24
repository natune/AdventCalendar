"""認証関連モジュール"""
from flask_login import LoginManager

from app.models import LoginUser, db

login_manager = LoginManager()


def init_app(app):
    """アプリケーションの初期化を行う

    Args:
        app (flask.app.Flask): 初期化を行うアプリケーション
    """
    app.secret_key('hoge')
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """ユーザの読み込みを行う

    Args:
        user_id (str): ユーザのログインID
    Returns:
        app.models.LoginUser: ユーザIDが一致したLoginUserオブジェクト
    """
    login_user = db.session.query(LoginUser).filter(
        LoginUser.login_id == user_id).first()
    return login_user
