# coding:utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init(_app):
    # 初始化 DB 配置
    db.app = _app
    db.init_app(_app)
