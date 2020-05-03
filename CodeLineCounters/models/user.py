# coding:utf-8
from CodeLineCounters.models import db
from werkzeug.security import generate_password_hash, check_password_hash



class Users(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20))
    user = db.Column(db.String(10))
    pwd = db.Column(db.String(128))

    def set_password(self, password):
        self.pwd = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.pwd, password)
