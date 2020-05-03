# coding:utf-8
from CodeLineCounters.models import db

class Record(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)
    line = db.Column(db.Integer)
    ctime = db.Column(db.Date)
    user_id = db.Column(db.Integer)
