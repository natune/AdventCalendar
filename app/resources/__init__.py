"""APIの管理モジュール"""
from flask_restful import Api

from app.resources.login import LoginResource


def init_app(app):
    """アプリケーションの初期化

    Args:
        app (flask.app.Flask): 初期化を行うアプリケーション
    """
    api = Api(app)

    resources = [(LoginResource, '/api/login')]

    for resource, url in resources:
        api.add_resource(resource, url)
