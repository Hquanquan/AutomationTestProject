#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 13:56
# @File : test_contract.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 测试合同类
import allure
import pytest

from 我的代码.pylib.utils.commom import dynamic_report
from 我的代码.pylib.utils.convertData import ConvertData
from 我的代码.pylib.webapi.contractsAPI import ContractsAPI


@allure.epic("API模块")
@allure.feature("合同-ContractsAPI")
class TestContract:

    @pytest.fixture()
    def before_tc003001(self, admin_login):
        # 1、删除当前系统上所有的合同
        self.contracts_api = ContractsAPI(admin_login)
        self.contracts_api.delete_all()
        yield
        # 2、测试完成清除测试数据
        self.contracts_api.delete(self.new_contract["_id"])

    @dynamic_report('name', 'name')
    @allure.story("合同-ContractsAPI-添加合同")
    @allure.title("添加合同测试用例")
    @pytest.mark.parametrize("name,amount", ConvertData.get_param())
    def test_tc003001(self, name, amount, before_tc003001, inin_organiz, init_accounts, init_contract_type):
        """
        当前系统没有合同，添加合同。预期结果是添加的合同存在于所有的合同列表中
        添加合同需要的参数：
            name string 合同名称
            othercompany string 签约对象ID
            contract_type string 合同类型ID
            company_id sting  分部ID
            create_date string 创建日期： 2020-07-07T07:31:06.754Z
            amount int 合同金额
        :param name: 参数化传入的name
        :param amount: 参数化传入的amount
        :param before_tc003001: 环境初始化
        :param inin_organiz: 提供部门对象信息
        :param init_accounts: 提供签约对象信息
        :param init_contract_type: 提供合同分类对象信息
        :return:
        """
        # 添加合同
        self.new_contract = self.contracts_api.add(name=name,
                                                   amount=amount,
                                                   othercompany=init_accounts[1]["_id"],
                                                   contract_type=init_contract_type["_id"],
                                                   company_id=inin_organiz[1]["_id"])
        # 列出所有合同
        contracts = self.contracts_api.list_all()
        # 断言 新添加的合同在所有合同里
        assert self.new_contract in contracts

    @pytest.fixture()
    def before_tc003052(self, admin_login):
        self.contracts_api = ContractsAPI(admin_login)
        # 1、删除当前系统上所有的合同
        self.contracts_api.delete_all()

    @allure.story("合同-ContractsAPI-修改合同")
    @allure.title("修改合同测试用例")
    def test_tc003052(self, before_tc003052):
        """
        当前系统不存在合同，通过一个不存在的合同ID去修改合同名称,预计结果是返回错误信息
        :param before_tc003052: 环境初始化，删除所有合同
        :return:
        """
        self.edit_contract = self.contracts_api.edit('self.new_contract["_id"]', name="新修改的名称")
        assert self.edit_contract["error"]["code"] == 500

    @pytest.fixture()
    def before_tc003091(self, admin_login, inin_organiz, init_accounts, init_contract_type):
        self.cookies = admin_login
        # 实例化合同对象
        self.contracts_api = ContractsAPI(self.cookies)
        # 删除所有合同
        self.contracts_api.delete_all()
        # 创建一个新合同
        self.new_contract = self.contracts_api.add(name="租房合同",
                                                   othercompany=init_accounts[1]["_id"],
                                                   contract_type=init_contract_type["_id"],
                                                   company_id=inin_organiz[1]["_id"],
                                                   create_date=ConvertData.current_time(),
                                                   amount=10000,
                                                   )

    # @pytest.mark.skip(reason='我就是不需要执行下面的接口')  # 一定不执行下面的接口
    # @pytest.mark.skipif(1 == 2, reason='我就是不需要执行下面的接口')  # 条件为真，就跳过，现在不为真，不跳过
    @allure.story("合同-ContractsAPI-删除合同")
    @allure.title("删除合同测试用例")
    def test_tc003091(self, before_tc003091):
        """
        当前系统没有合同，创建一个合同，通过该合同id删除合同。预期结果合同列表为空
        :param before_tc003091: 初始化环境，删除所有合同，创建一个新合同
        :return:
        """
        self.contracts_api.delete(self.new_contract["_id"])
        contracts2 = self.contracts_api.list_all()
        assert contracts2 == []
