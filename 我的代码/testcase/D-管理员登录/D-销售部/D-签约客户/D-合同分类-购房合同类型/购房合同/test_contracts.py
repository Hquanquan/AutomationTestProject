#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 17:28
# @File : test_contracts.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有合同
import pprint

import allure
import pytest

from 我的代码.pylib.utils.convertData import ConvertData


@allure.epic("API模块")
@allure.feature("合同-ContractsAPI")
class TestContracts:

    @pytest.fixture()
    def after_tc003002(self, init_contracts):
        """
        清除创建的合同测试数据
        :param init_contracts:
        :return:
        """
        self.contracts_api = init_contracts
        yield
        self.contracts_api.delete(self.new_contract["_id"])

    @allure.story("合同-ContractsAPI-添加合同")
    @allure.title("添加合同测试用例")
    def test_tc003002(self, after_tc003002, inin_organiz, init_accounts, init_contract_type):
        """
        当前系统已有合同，添加一个合同
        :param after_tc003002: 初始化环境，提供合同对象，清除测试数据
        :param inin_organiz: 提供部门对象信息
        :param init_accounts: 提供签约对象信息
        :param init_contract_type: 提供合同分类对象信息
        :return:
        """
        self.new_contract = self.contracts_api.add(name="租房合同",
                                                   othercompany=init_accounts[1]["_id"],
                                                   contract_type=init_contract_type[1]["_id"],
                                                   company_id=inin_organiz[1]["_id"],
                                                   create_date=ConvertData.current_time(),
                                                   amount=10000,
                                                   )
        contracts = self.contracts_api.list_all()
        assert self.new_contract in contracts

    @pytest.fixture()
    def before_tc003051(self, init_contracts, inin_organiz, init_accounts, init_contract_type):
        """
        1、环境初始化，系统已存在合同，创建一个不同的合同
        2、清除测试数据
        :param init_contracts: 创建一个合同，并提供合同实例对象
        :param inin_organiz: 提供部门对象信息
        :param init_accounts: 提供签约对象信息
        :param init_contract_type: 提供合同分类信息
        :return:
        """
        self.contracts_api = init_contracts
        self.new_contract = self.contracts_api.add(name="租房合同",
                                                   othercompany=init_accounts[1]["_id"],
                                                   contract_type=init_contract_type[1]["_id"],
                                                   company_id=inin_organiz[1]["_id"],
                                                   create_date=ConvertData.current_time(),
                                                   amount=10000,
                                                   )
        yield
        self.contracts_api.delete(self.new_contract["_id"])

    @allure.story("合同-ContractsAPI-修改合同")
    @allure.title("修改合同测试用例")
    def test_tc003051(self, before_tc003051):
        """
        当前系统已经有合同,修改合同的名称为"卖房合同"，只需传递name字段
        :param before_tc003051: 环境初始化，系统已存在合同，创建一个不同的合同
        :return:
        """
        # create_date = self.new_contract["create_date"] , create_date=create_date
        self.contracts_api.edit(self.new_contract["_id"], name="卖房合同")
        contracts = self.contracts_api.list_all()
        for i in contracts:
            if i["_id"] == self.new_contract["_id"]:
                assert i["name"] == "卖房合同"

    # @pytest.mark.skip("暂不执行")
    @allure.story("合同-ContractsAPI-删除合同")
    @allure.title("删除合同测试用例")
    def test_tc003092(self, init_contracts):
        """
        当前系统已有合同，通过不存在的合同ID删除合同。预期结果合同列表没发生变化
        :param init_contracts:
        :return:
        """
        self.contracts_api = init_contracts
        contracts1 = self.contracts_api.list_all()
        self.contracts_api.delete("fha不存在的合同IDsjfds")
        contracts2 = self.contracts_api.list_all()
        assert contracts1 == contracts2


