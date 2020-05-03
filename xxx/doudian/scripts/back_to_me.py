# encoding: utf-8
from scripts.quick_switch import QuickSwitch

import sys

if len(sys.argv) != 3:
    print u'\nUsage： \npython back_to_me.py   <你的浏览器cookie> <你的employee ID>'
    sys.exit(1)

people_name = unicode(sys.argv[1], 'utf-8')
session = sys.argv[1]
employee_id = sys.argv[2]

qs = QuickSwitch(session, employee_id)

qs.print_my_info(employee_id)

qs.active_myself()

print u"[DONE] 我又是我了，颜色不一样的烟火! \n[BE HAPPY]".format()
