#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 11:55
# @File : accountsAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pprint

from 我的代码.conf.env import email, password
from 我的代码.pylib.webapi.baseApi import BaseAPI
from 我的代码.pylib.webapi.user import User


class AccountsAPI(BaseAPI):
    """
    签约对象API,继承自BaseAPI,BaseAPI已实现CRUD增删改查功能。
    若需要扩展可在该类进行扩展，重写，重载
    """
    pass

if __name__ == '__main__':
    mycookies = User(email, password).login()
    org_api = AccountsAPI(mycookies)
    pprint.pprint(org_api.conf)
    pass