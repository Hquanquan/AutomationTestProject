#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 14:50
# @File : TestOrganizApi.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest



@allure.epic("API模块")
@allure.feature("部门-OrganizAPI")
class TestOrganizAPI:

    @pytest.fixture()
    def before_tc000001(self, empty_organiz):
        """
        环境初始化以及清除产生的测试数据
        """
        self.org_api = empty_organiz
        yield
        # 5、测试通过后清除测试生成的数据（删除新增的部门)
        self.org_api.delete(self.new_org["_id"])

    @allure.story("部门-OrganizAPI-添加部门")
    @allure.title("添加部门测试用例")
    def test_tc000001(self, before_tc000001):
        """
        当前公司没有分部门，添加公司分部
        :param before_tc000001:
        :return:
        """
        # step1 创建一个新的部门
        self.new_org = self.org_api.add(name="测试部")
        # step2 列出所有部门
        orgs = self.org_api.list_all()
        # step3 判断新创建的部门是否出存在所有的部门中
        assert self.new_org in orgs

    @pytest.fixture()
    def before_tc000091(self, empty_organiz):
        self.org_api = empty_organiz
        self.new_org = self.org_api.add(name="背锅部")

    @allure.story("部门-OrganizAPI-删除部门")
    @allure.title("删除部门测试用例")
    def test_tc000091(self, before_tc000091):
        """
        当前没有分部，创建一个部门，删除这个部门
        :return:
        """
        self.org_api.delete(self.new_org["_id"])
        # 列出所有部门，若为空则断言成功
        res = self.org_api.list_all()[1:]  # 过滤掉总公司
        assert res == []

