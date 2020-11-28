'''
@author: haiwen
@date: 2020/11/20
@file: conftest.py
'''
import pytest

from pylib.webapi.bussiness import OrganizAPI
from pylib.webapi.common import login
from conf.env import global_psw,global_email

@pytest.fixture(scope='session')
def admin_login():
    cookies=login(global_email,global_psw)
    return cookies

#清除所有部门数据
@pytest.fixture(scope='session')
def empty_organiz(admin_login):
    cookies = admin_login
    org_api = OrganizAPI(cookies)
    org_api.delete_all()
    return org_api