# encoding: utf-8
from scripts import env_config

import sys

from scripts.star_quick_switch import QuickSwitch

if len(sys.argv) != 5:
    print u'\nUsage： \npython star_one_click_switch.py <待切换的星图ID（切会管理员自己，输入0）> <csrtoken> <sessionid> <proxy_info: http://ip:port>'
    sys.exit(1)

star_id = sys.argv[1]
csrtoken = sys.argv[2]
session = sys.argv[3]
proxy_str = sys.argv[4]



qs = QuickSwitch(csrtoken, session, proxy_str)
if star_id == "0":
    star_id = u"当前管理员自己！"
    qs.switch_back()

else:
    qs.switch_back()

    qs.switch_to(star_id)


print u"期望切换的star_id : \n           >>>>>>>    {}  ".format(star_id)
