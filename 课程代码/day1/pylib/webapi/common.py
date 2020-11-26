"""
@author: haiwen
@date: 2020/11/20
@file: common.py
"""
import requests
from 课程代码.day1.conf.env import host, global_psw, global_email


def login(email, psw):
    path = '/accounts/password/authenticate'
    payload = {"user": {"email": email},
               "password": psw,
               "code": "",
               "locale": "zhcn"
               }
    resp = requests.post(f'{host}{path}', json=payload)
    # 登录需要返回什么？获取鉴权信息--cookies
    return resp.cookies


if __name__ == '__main__':
    pass
    # cookies = login(global_email, global_psw)
    # print(cookies['X-Space-Id'])
