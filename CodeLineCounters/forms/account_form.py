# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired(message=u"用户名不能为空")], render_kw={'placeholder': 'username'})
    password = PasswordField(u'密码', validators=[DataRequired(message=u"密码不能为空")], render_kw={'placeholder': 'password'})
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

class RegisterForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired(message=u"用户名不能为空")], render_kw={'placeholder': 'username'})
    nickname = StringField(u'昵称', validators=[DataRequired(message=u"昵称不能为空")], render_kw={'placeholder': 'nickname'})
    password = PasswordField(u'密码', validators=[DataRequired(message=u"密码不能为空")], render_kw={'placeholder': 'password'})
    password_confirm = PasswordField(u'重复密码', validators=[DataRequired(message=u"重复密码不能为空")], render_kw={'placeholder': 'confirm password'})
    submit = SubmitField(u'注册')


