"""Bulueprintの管理を行うモジュール"""
from app.views.login_view import login_page

def init_app(app):
    """アプリケーションの初期化を行う

    Args:
        app (flask.app.Flask): 初期化を行うアプリケーション
    """
    app.register_blueprint(login_page)
