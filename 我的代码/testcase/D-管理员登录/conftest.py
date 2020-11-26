#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 14:48
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from 我的代码.conf.env import email, password
from 我的代码.pylib.webapi.organuzAPI import OrganizAPI

from 我的代码.pylib.webapi.user import User


@pytest.fixture(scope='session')
def admin_login():
    cookies = User(email, password).login()
    return cookies


# 清除所有部门数据
@pytest.fixture(scope='session')
def empty_organiz(admin_login):
    cookies = admin_login
    org_api = OrganizAPI(cookies)
    org_api.delete_all()
    yield org_api
