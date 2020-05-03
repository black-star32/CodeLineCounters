# coding: utf-8

# import hashlib
#
#
# # 加密
# # hash = hashlib.md5(b'sdf1232sd')
# #
# # hash.update(bytes('123'))
# #
# # ret = hash.hexdigest()
# #
# # print ret
#
#
# import pymysql
# #    SQLALCHEMY_DATABASE_URI = "{}://root:Fengbo123@127.0.0.1:3306/black?charset=utf8mb4".format(mysql_protocal)
#
# conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Fengbo123',
#                        database='codeline', charset='utf8')
#
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# # sql = "select * from user_info where user='%s' and pwd='%s'"%('userA', 'af1c2e34d648e7df96d7bfdc3c4b243b')
# # print sql
#
# cursor.execute("select * from user_info where user=%s and pwd=%s", ('userA', 'af1c2e34d648e7df96d7bfdc3c4b243b'))
#
# # data = cursor.fetchall()
# data = cursor.fetchone()
#
# cursor.close()
# conn.close()
#
# print data

# 解压文件
import zipfile

origin_path = "/Users/fengbo/PycharmProjects/flask_demos/CodeLineCounters/files/doudian.zip"
target_path = "/Users/fengbo/PycharmProjects/flask_demos/CodeLineCounters/xxx"
zip_file = zipfile.ZipFile(origin_path)
zip_list = zip_file.namelist()  # 得到压缩包里所有文件

for f in zip_list:
    zip_file.extract(f, target_path)  # 循环解压文件到指定目录

zip_file.close()  # 关闭文件，必须有，释放内存
