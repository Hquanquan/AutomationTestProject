#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 10:13
# @File : test_contractTypes.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有合同分类
import allure
import pytest

@allure.epic("API模块")
@allure.feature("合同分类-ContractTypesAPI")
class Test_contractTypes:

    @pytest.fixture()
    def after_tc002002(self, init_contract_type):
        self.contractType_api = init_contract_type[0]
        yield
        self.contractType_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-添加合同分类")
    @allure.title("添加合同分类测试用例")
    def test_tc002002(self, after_tc002002):
        """
        当前系统已有合同分类，创建一个不同的合同分类
        :param after_tc002002:
        :return:
        """
        self.new_contractType = self.contractType_api.add(name="租赁合同类型", code="20201126001")
        contractTypes = self.contractType_api.list_all()
        assert self.new_contractType in contractTypes

    @pytest.fixture()
    def before_tc002051(self, init_contract_type):
        self.contractType_api = init_contract_type[0]
        self.new_contractType = self.contractType_api.add(name="租赁合同类型", code="20201126001")
        yield
        self.contractType_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-修改合同分类")
    @allure.title("修改合同分类测试用例")
    def test_tc002051(self, before_tc002051):
        self.contractType_api.edit(self.new_contractType["_id"], name="合同类型-未分类")
        contractTypes = self.contractType_api.list_all()
        for item in contractTypes:
            if item["_id"] == self.new_contractType["_id"]:
                assert item["name"] == "合同类型-未分类"
                break

    @allure.story("合同分类-ContractTypesAPI-删除合同分类")
    @allure.title("删除合同分类测试用例")
    def test_tc002092(self, init_contract_type):
        """
        当前系统已有合同，通过不存在的合同分类id删除合同分类
        :param init_contract_type:
        :return:
        """
        self.contractType_api = init_contract_type[0]
        contractTypes1 = self.contractType_api.list_all()
        res = self.contractType_api.delete("不存在的合同分类id")
        contractTypes2 = self.contractType_api.list_all()
        assert contractTypes1 == contractTypes2

