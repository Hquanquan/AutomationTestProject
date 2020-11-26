#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:49
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest
from 我的代码.pylib.webapi.accountsAPI import AccountsAPI
from 我的代码.pylib.webapi.contractTypesAPI import ContractTypesAPI
@pytest.fixture(scope="package")
def init_accounts(admin_login, inin_organiz):
    """
    创建签约对象
    创建签约对象需要的参数：
        "name": name, 签约对象名称
        "category": 1, 签约对象类别，企业：1，个人：2，其他：3
        "company_ids": ["QmBLZC5zKaEMu96QN"],关联部门ID
        "status": 1, 启用状态，未启用：1，已启用：2 ，停用：3
        "space": self.api.space, spaceid可以从cookies的X-Space-Id字段获取
    测试完成后需要删除测试产生的数据，所以调用删除delete()
    :param admin_login: 提供cookies
    :param inin_organiz: 提供销售部对象
    :return:
    """
    sale_org = inin_organiz[1]
    accounts_api = AccountsAPI(admin_login)
    accounts_api.delete_all()
    vip_account = accounts_api.add(name="VIP客户", company_ids=[sale_org["_id"]])
    yield accounts_api, vip_account
    accounts_api.delete(vip_account["_id"])

@pytest.fixture(scope="package")
def empty_contractType(admin_login):
    """
    清除当前系统的中合同分类
    :param admin_login:
    :return:
    """
    contractType_api = ContractTypesAPI(admin_login)
    contractType_api.delete_all()
    yield contractType_api
