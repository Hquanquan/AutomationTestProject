#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 17:17
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from 我的代码.pylib.utils.convertData import ConvertData
from 我的代码.pylib.webapi.contractsAPI import ContractsAPI


@pytest.fixture(scope="package")
def init_contracts(admin_login, inin_organiz, init_accounts, init_contract_type):
    """
    1、创建合同
    2、测试后删除该测试数据
    :param admin_login: 提供cookies
    :param inin_organiz: 提供部门对象信息
    :param init_accounts: 提供签约对象信息
    :param init_contract_type: 提供合同分类对象信息
    :return:
    """
    contracts_api = ContractsAPI(admin_login)
    contracts_api.delete_all()
    new_contract = contracts_api.add(name="购房合同",
                                     othercompany=init_accounts[1]["_id"],
                                     contract_type=init_contract_type["_id"],
                                     company_id=inin_organiz[1]["_id"],
                                     create_date=ConvertData.current_time())
    # create_date = ConvertData.current_time() 以特格式指定当前时间
    yield contracts_api
    contracts_api.delete(new_contract["_id"])
