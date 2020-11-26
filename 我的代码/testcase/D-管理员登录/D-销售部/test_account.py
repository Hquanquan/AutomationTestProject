#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 14:10
# @File : test_account.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有签约客户
import allure
import pytest


@allure.epic("API模块")
@allure.feature("签约对象-AccountsAPI")
class TestAccounts:

    @pytest.fixture()
    def before_tc001001(self, empty_accounts):
        self.accounts_api = empty_accounts
        yield
        self.accounts_api.delete(self.new_account["_id"])

    @allure.story("签约对象-AccountsAPI-添加签约对象")
    @allure.title("添加签约对象测试用例")
    def test_tc001001(self, before_tc001001, inin_organiz):
        """
        当前公司没有签约对象，创建一个签约客户
        :param before_tc001001:  环境初始化，删除系统所有合同，清除测试后的数据
        :param inin_organiz: 提供部门对象信息
        :return:
        """
        self.new_account = self.accounts_api.add(name="SVIP客户", company_ids=[inin_organiz[1]["_id"]])
        accounts = self.accounts_api.list_all()
        assert self.new_account in accounts

    @allure.story("签约对象-AccountsAPI-修改签约对象")
    @allure.title("修改签约对象测试用例tc001052")
    def test_tc001052(self, empty_accounts):
        """
        当前系统没有签约对象，通过不存在的签约对象id类修改签约对象
        :param empty_accounts: 环境初始化，清除系统中的签约对象
        :return:
        """
        self.accounts_api = empty_accounts
        res = self.accounts_api.edit("asdf不存在的idh1", name="金主")
        assert res["error"]["code"] == 500

    @pytest.fixture()
    def before_tc001091(self, empty_accounts, inin_organiz):
        self.accounts_api = empty_accounts
        self.new_account = self.accounts_api.add(name="SVIP客户", company_ids=[inin_organiz[1]["_id"]])
        yield

    @allure.story("签约对象-AccountsAPI-删除签约对象")
    @allure.title("删除签约对象测试用例tc001091")
    def test_tc001091(self, before_tc001091):
        """
        当前系统没有签约对象，通过一个已存在的签约对象id删除签约对象
        :param before_tc001091:
        :return:
        """
        self.accounts_api.delete(self.new_account["_id"])
        res = self.accounts_api.list_all()
        assert res == []

