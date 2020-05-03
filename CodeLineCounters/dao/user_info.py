# coding:utf-8
from CodeLineCounters.models import db
from CodeLineCounters.models.user import Users

class UserDao():

    def create_user_info(self, form):
        user = Users()
        user.user = form.username.data
        user.nickname = form.nickname.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

    def validate_user_info(self, form):
        user = db.session.query(Users).filter(Users.user==form.username.data).first()
        if not user:
            return None, None
        if user.validate_password(form.password.data):
            return user.id, user.nickname

    def get_user_info(self):
        user_list = db.session.query(Users).all()
        return user_list
