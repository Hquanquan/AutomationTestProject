#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 12:45
# @File : user.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import requests


from 我的代码.conf.env import HOST, email, password


# 登录函数，可直接调用
def login(email, psw):
    path = "/accounts/password/authenticate"
    payload = {
        "user": {"email": email},
        "password": psw,
        "code": "",
        "locale": "zhcn"
    }
    url = f"{HOST}{path}"
    resp = requests.post(url, json=payload)
    return resp.cookies



class User:

    def __init__(self, email, psw):
        self.host = HOST
        self.email = email
        self.psw = psw

    def login(self):
        path = "/accounts/password/authenticate"
        payload = {
            "user": {"email": self.email},
            "password": self.psw,
            "code": "",
            "locale": "zhcn"
        }
        url = f"{self.host}{path}"
        resp = requests.post(url, json=payload)
        return resp.cookies


if __name__ == '__main__':
    user = User("test_587@test.com", "123456")
    print(user.login())
