"""
@author: haiwen
@date: 2020/11/20
@file: conftest.py
"""
import pytest

from 课程代码.day1.pylib.webapi.OrganizApiLib import OrganizApi
from 课程代码.day1.pylib.webapi.common import login
from 课程代码.day1.conf.env import global_psw, global_email


@pytest.fixture(scope='session')
def admin_login():
    cookies = login(global_email, global_psw)
    return cookies
