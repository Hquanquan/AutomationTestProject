#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 16:01
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import pytest

from 我的代码.pylib.webapi.organuzAPI import OrganizAPI
from 我的代码.pylib.webapi.accountsAPI import AccountsAPI

@pytest.fixture(scope="session")
def inin_organiz(admin_login):
    """
    初始化：创建销售部。
    测试完成后清除测试数据
    :param admin_login:
    :return:
    """
    cookies = admin_login
    org_api = OrganizAPI(cookies)
    org_api.delete_all()
    sale_org = org_api.add(name="销售部")
    yield org_api, sale_org
    org_api.delete(sale_org["_id"])

@pytest.fixture(scope="session")
def empty_accounts(admin_login):
    accounts_api = AccountsAPI(admin_login)
    accounts_api.delete_all()
    yield accounts_api
