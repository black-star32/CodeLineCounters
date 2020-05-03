# coding:utf-8
from CodeLineCounters.models import db
from CodeLineCounters.models.record import Record

class RecordDao():

    def get_user_record_list(self, user_id):
        record_list = db.session.query(Record).filter(Record.user_id==user_id).all()
        return record_list

    def check_user_record(self, ctime, user_id):
        result = db.session.query(Record).filter(Record.ctime==ctime, Record.user_id==user_id).first()
        return result

    def create_user_record(self, total_num, ctime, user_id):
        record = Record(line=total_num, ctime=ctime, user_id=user_id)
        db.session.add(record)
        db.session.commit()
