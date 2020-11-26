#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 13:56
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest
from 我的代码.pylib.webapi.contractTypesAPI import ContractTypesAPI

@pytest.fixture(scope="session")
def init_contract_type(admin_login):
    """
    初始化：创建合同分类，创建合同分类所需参数：
        space：工作区ID
        name：合同名
        code：合同编码
    :param admin_login: 提供cookies
    :return:
    """
    cookies = admin_login
    # 实例化合同分类对象
    contype_api = ContractTypesAPI(cookies)
    contype_api.delete_all()
    # 创建一个合同分类
    cta = contype_api.add(name="购房合同", space="20201124")
    yield cta
    contype_api.delete(cta["_id"])
