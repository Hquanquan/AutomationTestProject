"""
@author: haiwen
@date: 2020/11/23
@file: conftest.py
"""
import pytest

from 课程代码.day3.pylib.webapi.bussiness import AccountsAPI


@pytest.fixture(scope='package')
def init_accounts(admin_login, init_organiz):
    sale_org = init_organiz
    account_api = AccountsAPI(admin_login)
    vip_account = account_api.add(name='VIP客户', company_ids=[sale_org['_id']])
    yield vip_account
    account_api.delete(vip_account['_id'])
