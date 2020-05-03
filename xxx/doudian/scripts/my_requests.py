# encoding: utf-8
import json

import requests as requests


class MyRequests(object):
    u'''封装requests， 打印请求详情'''

    @staticmethod
    def get(url, headers=None, cookies=None, params=None, debug=False):
        u'HTTP get 请求，default cookie: fake_employ_id fetched from current_info.employee_id'

        req = requests.get(url, headers=headers, cookies=cookies, params=params)

        if debug:
            # print request details
            MyRequests().log_request_details(url, headers=headers, cookies=cookies, params=params)

            # print response details
            MyRequests().log_response_details(req)

        return req

    @staticmethod
    def post(url, headers=None, params=None, cookies=None, data=None, debug=False, proxies=None, is_json=False):
        u"HTTP post请求，有打印 default cookie: fake_employ_id fetched from current_info.employee_id"

        if is_json:
            json_header = {"content_type": "application/json"}
            headers.update(json_header)
            data = json.dumps(data)

        req = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, proxies=proxies)
        if debug:
            # print request details
            MyRequests().log_request_details(url, headers=headers, cookies=cookies, params=params, data=data)
            # print response details
            MyRequests().log_response_details(req)

        return req

    def log_request_details(self, url=None, headers=None, cookies=None, params=None, data=None):
        print("-----[REQUEST] details below : ----------------------------")

        print("  Request : {}".format(url))
        if headers != None:
            print("  Headers : {}".format(headers))
        if cookies != None:
            print("  Cookies : {}".format(cookies))
        if params != None:
            print("  Parameters : {}".format(params.__repr__().decode("unicode-escape")))
        if data != None:
            print(u"  Payload : {}".format(data.__repr__().decode("unicode-escape")))

    def log_response_details(self, response_body):
        print(
            " -----[RESPONSE] details below : ----------------------------")

        print '  Returned code: {}'.format(response_body.status_code)

        if response_body.status_code != 200:
            print(
                "[WARN]Return code is not 200!!!! but {} .".format(
                    response_body.status_code))

            err_msg = response_body.text
            try:
                json_body = response_body.json()
                s = str(json_body).replace('u\'', '\'')
                print '  Response: '
                print  s.decode('unicode-escape')
                err_msg = s.decode('unicode-escape')

            except:
                print '  Response raw data: \n{}'.format(err_msg)

            raise Exception(u"检查请求细节是否出错，或者服务器是否有问题\n{}".format(err_msg))

        else:
            try:
                json_body = response_body.json()
                s = str(json_body).replace('u\'', '\'')
                print '  Response: '
                print  s.decode('unicode-escape')

            except:
                print u'  Response raw data: \n{}'.format(response_body.text)
                raise Exception(u"http请求的返回不是Json格式，检查服务器是否有问题")

        print("------------------------------------------------------------------------")


if __name__ == '__main__':
    HOSTNAME = "https://con-test.bytedance.net"
    CUSOMTER_INFO_URL = "https://con-test.bytedance.net/back_end/contract/ka_agent/create/agent"  # HOSTNAME + "/back_end/contract/ka_agent/create/agent"
