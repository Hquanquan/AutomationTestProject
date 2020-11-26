"""
@author: haiwen
@date: 2020/11/23
@file: conftest.py
"""
import pytest

from 课程代码.day3.pylib.webapi.bussiness import ContractTypesAPI


@pytest.fixture(scope='session')
def init_contract_type(admin_login):
    contype_api = ContractTypesAPI(admin_login)
    cta = contype_api.add(name='购房合同', code='20201123')
    yield cta
    contype_api.delete(cta['_id'])
