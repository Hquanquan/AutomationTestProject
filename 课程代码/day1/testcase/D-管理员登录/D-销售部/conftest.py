"""
@author: haiwen
@date: 2020/11/20
@file: conftest.py
"""
import pytest

# 创建销售部
from 课程代码.day1.pylib.webapi.OrganizApiLib import OrganizApi

@pytest.fixture(scope="session")
def init_organiz(admin_login):
    cookies = admin_login
    org_api = OrganizApi(cookies)
    sale_org = org_api.add("销售部")
    yield org_api
    org_api.delete(sale_org["_id"])

