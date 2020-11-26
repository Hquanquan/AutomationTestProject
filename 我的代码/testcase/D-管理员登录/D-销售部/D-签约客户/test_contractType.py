#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 9:56
# @File : test_contractType.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有合同分类
import allure
import pytest

@allure.epic("API模块")
@allure.feature("合同分类-ContractTypesAPI")
class Test_ContractTypesAPI:

    @pytest.fixture()
    def after_tc002001(self, empty_contractType):
        self.contractType_api = empty_contractType
        yield
        self.contractType_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-添加合同分类")
    @allure.title("添加合同分类测试用例")
    def test_tc002001(self, after_tc002001):
        """
        当前系统没有合同分类，创建一个合同分类
        :param after_tc002001: 初始化环境，提供一个合同分类实例对象
        :return:
        """
        self.new_contractType = self.contractType_api.add(name="房产合同类型", code="20201126")
        contractTypes = self.contractType_api.list_all()
        assert self.new_contractType in contractTypes

    @allure.story("合同分类-ContractTypesAPI-修改合同分类")
    @allure.title("修改合同分类测试用例")
    def test_tc002052(self, empty_contractType):
        """
        当前系统没有合同分类，通过一个不存在的合同分类ID编辑合同分类
        :param empty_contractType: 环境初始化，删除系统中的合同分类，提供合同分类实例对象
        :return:
        """
        self.contractType_api = empty_contractType
        res = self.contractType_api.edit("sdf不存在的合同分类idfadsf", name="合同分类名称")
        assert res["error"]["code"] == 500

    @pytest.fixture()
    def before_tc002091(self, empty_contractType):
        self.contractType_api = empty_contractType
        self.new_contractType = self.contractType_api.add(name="房产合同类型", code="20201126")
        yield
        self.contractType_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-删除合同分类")
    @allure.title("删除合同分类测试用例")
    def test_tc002091(self, before_tc002091):
        res = self.contractType_api.delete(self.new_contractType["_id"])
        contractTypes = self.contractType_api.list_all()
        assert contractTypes == []
