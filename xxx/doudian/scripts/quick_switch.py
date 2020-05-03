# encoding: utf-8
import pymysql
from scripts import env_config
from scripts.my_requests import MyRequests
import sys


class QuickSwitch:
    HOSTNAME = env_config.BSM_HOSTNAME
    ACTIVE_MYSELF_URL = HOSTNAME + "/back_end/authorization/activate_self/"
    ACTIVE_URL = HOSTNAME + "/back_end/authorization/activate/"
    GET_AUTH_LIST_URL = HOSTNAME + "/back_end/authorization/in_list/?limit=100"
    DEFAULT_VALID_DAY = env_config.DEFAULT_VALID_DAY

    hostname = env_config.BSM_DB_DICT.get('host')
    db_port = env_config.BSM_DB_DICT.get('port')
    username = env_config.BSM_DB_DICT.get('user')
    password = env_config.BSM_DB_DICT.get('password')
    schema = env_config.BSM_DB_DICT.get('database')
    dbconn = pymysql.connect(host=hostname, db=schema, user=username, passwd=password, port=db_port, charset='utf8')
    cursor = dbconn.cursor()

    DEFAULT_HEADER = None
    MY_ID = None

    def __init__(self, cookie, employee_id):
        self.MY_ID = employee_id
        self.DEFAULT_HEADER = {"Cookie": "login_token={}".format(cookie)}

    def active_myself(self):
        req = MyRequests.post(self.ACTIVE_MYSELF_URL, headers=self.DEFAULT_HEADER, debug=False)

        if req.status_code != 200:
            print (u"[ERROR] bsm 服务可能暂时挂了。。。再试一次")
            sys.exit(1)
        try:
            req.json()
        except:
            print (u"[ERROR] 你的login_token 可能过期了，去更新一下 my_info里面的 my_cookie 值")
            sys.exit(1)

    # input  名字
    # return  auth_id
    # def get_auth_id(self, people_name):
    #     # req = MyRequests.get(self.GET_AUTH_LIST_URL, headers=self.DEFAULT_HEADER, debug=False)
    #     # auth_list = req.json().get('data')
    #     # for people in auth_list:
    #     #     if people.get('authorizer_name') == people_name:
    #     #         auth_id = people.get('id')
    #     #         break;
    #     target_auth_employee_id = self.MY_ID
    #
    #     get_auth_id_statement = "select id from employee_authorization " \
    #                             "where authorized_id = {} and authorizer_id = {} " \
    #                             "and status = 1 and type=0 and is_cancel=0 " \
    #                             "and current_date() <= end_time and start_time <= current_date()   ".format(
    #         target_auth_employee_id, people.get_id(people_name))
    #     self.cursor.execute(get_auth_id_statement)
    #     rs = self.cursor.fetchone()
    #
    #     if rs is None:
    #         return None
    #     else:
    #         (db_auth_id,) = rs
    #         return db_auth_id

            # input  名字
            # return  auth_id

    def get_auth_id_by_people_id(self, people_id):
        # req = MyRequests.get(self.GET_AUTH_LIST_URL, headers=self.DEFAULT_HEADER, debug=False)
        # auth_list = req.json().get('data')
        # for people in auth_list:
        #     if people.get('authorizer_name') == people_name:
        #         auth_id = people.get('id')
        #         break;
        target_auth_employee_id = self.MY_ID

        get_auth_id_statement = "select id from employee_authorization " \
                                "where authorized_id = {} and authorizer_id = {} " \
                                "and status = 1 and type=0 and is_cancel=0 " \
                                "and current_date() <= end_time and start_time <= current_date()   ".format(
            target_auth_employee_id, people_id)
        self.cursor.execute(get_auth_id_statement)
        rs = self.cursor.fetchone()

        if rs is None:
            return None
        else:
            (db_auth_id,) = rs
            return db_auth_id

    def get_employe_name(self, people_id):

        get_auth_id_statement = "select name from employee where id ={}   ".format(people_id)
        self.cursor.execute(get_auth_id_statement)
        rs = self.cursor.fetchone()

        if rs is None:
            return None
        else:
            (people_name,) = rs
            return people_name

    def switch_to(self, auth_id, ):
        results = False
        if auth_id:
            data = {"id": auth_id}
            req = MyRequests.post(self.ACTIVE_URL, headers=self.DEFAULT_HEADER, data=data, debug=False)
            if req.json().get('success') == True:
                results = True

        return results

    def db_auth_insert(self, id):
        target_auth_employee_id = self.MY_ID

        if target_auth_employee_id is None or target_auth_employee_id == 0:
            print (u"[ERROR] 员工号不正确，更新自己的员工号到 my_info 里面的 my_employee_id ！！")
            sys.exit(1)

        get_name_statement = "select name from employee where id = %s" % (target_auth_employee_id)
        self.cursor.execute(get_name_statement)

        tester_name = self.cursor.fetchall()[0][0]

        insert_statement = u''' \
        INSERT INTO employee_authorization \
        (`authorizer_id`, `authorized_id`, `status`, `is_cancel`, `start_time`, `end_time`, `reason`, `creator_id`) \
        VALUES \
        (%d, %s, 1, 0, current_date(), date_add(current_date(),INTERVAL %d DAY), '[TEST]self-service auth switch by %s', %s);''' % (
            id, target_auth_employee_id, QuickSwitch.DEFAULT_VALID_DAY, tester_name, target_auth_employee_id)
        self.cursor.execute(insert_statement)

        self.dbconn.commit()

    def print_my_info(self, id):
        get_name_statement = "select name from employee where id = %s" % (id)
        self.cursor.execute(get_name_statement)

        rs = self.cursor.fetchone()

        if rs is None:
            print (u"[ERROR] 员工号 '{}' 找不到对应的人，更新自己的员工号到 my_info 里面的 my_employee_id ！！".format(id))
            sys.exit(1)
        else:
            (name,) = rs
            print u"你的个人信息: {} - {} ...".format(name, id)

    def close_db(self):
        self.cursor.close()
        self.dbconn.close()
