# encoding: utf-8
from scripts.quick_switch import QuickSwitch
from scripts import env_config

import sys

if len(sys.argv) != 4:
    print u'\nUsage： \npython one_click_switch.py <切换人的中文名字> <你的浏览器cookie> <你的employee ID>'
    sys.exit(1)

people_id =  sys.argv[1]
session = sys.argv[2]
employee_id = sys.argv[3]

qs = QuickSwitch(session, employee_id)

qs.print_my_info(employee_id)
people_name=qs.get_employe_name(people_id)
print u"期望切换的人物 : \n           >>>>>>>    {} - {}".format(people_name,people_id)


qs.active_myself()
auth_id = qs.get_auth_id_by_people_id(people_id)

if auth_id:
    pass
else:
    print (u"[INFO] 没有找到 '{}' 给你的授权记录。。。, 去BSM db给你加入一条授权。。".format(people_name))
    qs.db_auth_insert(int(people_id))
    auth_id = qs.get_auth_id_by_people_id(people_id)

if qs.switch_to(auth_id):
    print u"[DONE] 切换人物成功，你现在是  {} - {} \n[BE HAPPY] 默认生效 {} 天，如有需要，修改env里面的DEFAULT_VALID_DAY字段".format(people_id, people_name, env_config.DEFAULT_VALID_DAY)
else:
    print (u"[ERROR] 切换'{}' 失败， 检查代码。。。".format(people_name))
    sys.exit(1)

qs.close_db()
