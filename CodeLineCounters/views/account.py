# coding:utf-8
from flask import Blueprint, render_template, request, redirect, session, flash
from CodeLineCounters.utils.md5 import md5
from ..utils import helper
from ..forms.account_form import LoginForm, RegisterForm
# from CodeLineCounters.models import db
# from CodeLineCounters.models.user import Users
# from CodeLineCounters.models.record import Record
from CodeLineCounters.dao.user_info import UserDao

account = Blueprint('account', __name__)

@account.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        id, nickname = UserDao().validate_user_info(form)
        if not id:
            flash(u"用户名或密码错误")
            return redirect('/login')
        session['user_info'] = {'id':id,'nickname':nickname}
        return redirect('/home')

    return render_template('login.html', form=form)


    # if request.method == 'GET':
    #     form = LoginForm()
    #     return render_template('login.html', form=form)
    #
    # username = request.form.get('username')
    # password = request.form.get('password')
    #
    # pwd_md5 = md5(password)
    #
    #
    # """
    # 去数据库校验，校验成功写入session，不成功重定向主页
    # """
    # # import pymysql
    # # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
    # #                        database='codeline', charset='utf8')
    # # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # # cursor.execute("select id, nickname from user_info where user=%s and pwd=%s", (username, pwd_md5))
    # # data = cursor.fetchone()
    # # cursor.close()
    # # conn.close()
    #
    # data = helper.fetch_one("select id, nickname from user_info where user=%s and pwd=%s", (username, pwd_md5))
    #
    # if not data:
    #     return render_template('login.html', error="用户名或密码错误")
    # # session['user_info'] = {'id':data['id'],'nickname':data['nickname']}
    # session['user_info'] = data
    # return redirect('/home')

@account.route('/logout')
def logout():
    if "user_info" in session:
        del session['user_info']

    return redirect('/login')

@account.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_confirm.data:
            form = RegisterForm(username=form.username.data, nickname=form.nickname.data,
                                 password=form.password.data, password_confirm=form.password_confirm.data)
            flash(u'两次输入密码不一致')
            return render_template('register.html', form=form)
        UserDao().create_user_info(form)
        return redirect('/login')
    return render_template('register.html', form=form)
