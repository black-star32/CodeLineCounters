# encoding: utf-8
import json

from scripts import env_config
from scripts.my_requests import MyRequests


class QuickSwitch:
    HOSTNAME = env_config.STAR_TEST_HOSTNAME
    SWITCH_TO_URL = HOSTNAME + "/v/api/admin/mock/"

    DEFAULT_PROXY = {}
    DEFAULT_HEADER = {}

    def __init__(self, csrtoken, session_id, proxy_str):
        print "--------"

        headers = {}
        headers["X-CSRFToken"] = csrtoken
        headers["Cookie"] = "csrftoken={};sessionid={}".format(csrtoken, session_id)
        self.DEFAULT_HEADER = headers

        proxy = {"http": proxy_str}
        self.DEFAULT_PROXY = proxy

    def switch_to(self, target_star_id):
        results = False

        payload = {'mock_type': 2, 'value': (target_star_id)}
        print payload

        payload_json = json.dumps(payload)
        print payload_json


        print self.DEFAULT_HEADER
        print self.DEFAULT_PROXY
        req = MyRequests.post(self.SWITCH_TO_URL, headers=self.DEFAULT_HEADER, data=payload,
                              proxies=self.DEFAULT_PROXY,is_json=True)

        print "请求返回值  ： {}".format(req.status_code)


        return results

    def switch_back(self):
        results = False

        payload = {'mock_type': 0}
        print payload
        payload_json = json.dumps(payload)

        req = MyRequests.post(self.SWITCH_TO_URL, headers=self.DEFAULT_HEADER, data=payload_json,
                              proxies=self.DEFAULT_PROXY)

        print "请求返回值  ： {}".format(req.status_code)

        return results
