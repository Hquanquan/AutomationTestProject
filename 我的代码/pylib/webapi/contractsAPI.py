#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 11:47
# @File : contractsAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : ContractsAPI合同API,继承自BaseAPI,BaseAPI已实现CRUD增删改查功能。
#             若需要扩展可在该类进行扩展，重写，重载

import pprint

from 我的代码.conf.env import password, email
from 我的代码.pylib.webapi.baseApi import BaseAPI
from 我的代码.pylib.webapi.user import User


class ContractsAPI(BaseAPI):
    # def edit(self, _id, **kwargs):

    pass

if __name__ == '__main__':
    mycookies = User(email, password).login()
    org_api = ContractsAPI(mycookies)
    pprint.pprint(org_api.conf)
