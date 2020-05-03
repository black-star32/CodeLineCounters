# coding:utf-8
from flask import Flask
from flask_session import Session
from setting import config
from views.account import account
from views.index import ind


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    from CodeLineCounters.models import init
    init(app)

    app.register_blueprint(account)
    app.register_blueprint(ind)

    # Session(app)


    return app
