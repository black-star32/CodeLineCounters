# coding:utf-8
import os

from flask import Blueprint, redirect, session, render_template, request
import uuid
from ..utils import helper
from CodeLineCounters.dao.user_info import UserDao
from CodeLineCounters.dao.record import RecordDao

ind = Blueprint('ind', __name__)

@ind.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/login')
    return None

@ind.route('/')
def redirect_to_home():
    return redirect('/home')

@ind.route('/home')
def index():
    return render_template('home.html')


@ind.route('/user_list')
def user_list():
    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
    #                        database='codeline', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id,user,nickname from user_info")
    # data_list = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # data_list = helper.fetch_all("select id,user,nickname from user_info", [])
    data_list = UserDao().get_user_info()

    return render_template('user_list.html', data_list=data_list)

@ind.route('/detail/<int:nid>')
def detail(nid):
    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
    #                        database='codeline', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id, line, ctime from record where user_id=%s", (nid,))
    # record_list = cursor.fetchall()
    # cursor.close()
    # conn.close()
    record_list = RecordDao().get_user_record_list(nid)
    # record_list = helper.fetch_all("select id, line, ctime from record where user_id=%s", (nid,))

    return render_template('detail.html', record_list=record_list)

@ind.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    file_obj = request.files.get('code')
    print type(file_obj)
    print file_obj.filename
    print file_obj.stream

    # 1.检查上传文件的后缀名

    name_ext = file_obj.filename.rsplit('.', 1)

    if len(name_ext) != 2:
        return "请上传zip压缩文件"
    if name_ext[1] != 'zip':
        return "请上传zip压缩文件"
    """
    # 2.接收用户上传的文件，并写入到服务器本地
    file_path = os.path.join('files', file_obj.filename)
    # 从file_obj.stream中读取内容，再写入文件
    file_obj.save(file_path)

    # 3.解压zip文件
    import zipfile

    target_path = file_obj.filename
    zip_file = zipfile.ZipFile(file_path)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, target_path)  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存
    """
    # 2+3 接收用户上传文件，并解压到指定目录
    import zipfile
    target_path = os.path.join('files', str(uuid.uuid4()))
    zip_file = zipfile.ZipFile(file_obj.stream)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, target_path)  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存

    # 4.遍历某个目录下的所有文件
    total_num = 0
    for base_path, folder_list, file_list in os.walk(target_path):
        for filename in file_list:
            file_path = os.path.join(base_path, filename)
            file_ext = file_path.rsplit('.', 1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            # print file_num, file_path
            total_num += file_num
    # print total_num

    # 获取当前时间
    import datetime
    ctime = datetime.date.today()

    # import datetime
    # ctime = datetime.date.today()

    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
    #                        database='codeline', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id from record where ctime=%s and user_id=%s",
    #                (ctime, session['user_info']['id']))
    # data = cursor.fetchone()
    # cursor.close()
    # conn.close()
    # data = helper.fetch_one("select id from record where ctime=%s and user_id=%s",(ctime, session['user_info']['id']))

    data = RecordDao().check_user_record(ctime=ctime, user_id=session['user_info']['id'])

    if data:
        return "今天已经上传"



    # import pymysql
    # conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
    #                        database='codeline', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("insert into record(line,ctime,user_id)values(%s,%s,%s)",(total_num,ctime,session['user_info']['id']))
    # conn.commit()
    # cursor.close()
    # conn.close()
    # helper.insert("insert into record(line,ctime,user_id)values(%s,%s,%s)",(total_num,ctime,session['user_info']['id']))

    RecordDao().create_user_record(total_num=total_num, ctime=ctime, user_id=session['user_info']['id'])

    return "上传成功"
