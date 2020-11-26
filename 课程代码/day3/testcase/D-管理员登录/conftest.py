"""
@author: haiwen
@date: 2020/11/20
@file: conftest.py
"""
import pytest

from 课程代码.day3.conf.env import global_email, global_psw
from 课程代码.day3.pylib.webapi.bussiness import OrganizAPI
from 课程代码.day3.pylib.webapi.common import login


@pytest.fixture(scope='session')
def admin_login():
    cookies = login(global_email, global_psw)
    return cookies


# 清除所有部门数据
@pytest.fixture(scope='session')
def empty_organiz(admin_login):
    cookies = admin_login
    org_api = OrganizAPI(cookies)
    org_api.delete_all()
    return org_api
