#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 17:06
# @File : test_organiz.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest

@allure.epic("API模块")
@allure.feature("部门-OrganizAPI")
class Test_Organiz:

    @pytest.fixture()
    def after_tc000002(self, inin_organiz):
        self.org_api = inin_organiz[0]
        yield
        self.org_api.delete(self.new_org["_id"])

    @allure.story("部门-OrganizAPI-添加部门")
    @allure.title("添加部门测试用例")
    def test_tc000002(self, after_tc000002):
        """
        当前已有部门，新增一个部门
        :param after_tc000002:
        :return:
        """
        self.new_org = self.org_api.add(name="产品运营部")
        orgs = self.org_api.list_all()
        assert self.new_org in orgs

    @pytest.fixture()
    def before_tc000051(self, inin_organiz):
        self.org_api = inin_organiz[0]
        self.new_org = self.org_api.add(name="研发部")
        yield
        self.org_api.delete(self.new_org["_id"])

    @allure.story("部门-OrganizAPI-修改部门")
    @allure.title("修改部门测试用例")
    def test_tc000051(self, before_tc000051):
        """
        当前已有部门，修改部门的名称
        :param before_tc000051: 环境初始化，创建一个部门
        :return:
        """
        self.org_api .edit(_id=self.new_org["_id"], name="产品研发部")
        orgs = self.org_api.list_all()
        for org in orgs:
            if org["_id"] == self.new_org["_id"]:
                assert org["name"] == "产品研发部"
                break

    @allure.story("部门-OrganizAPI-修改部门")
    @allure.title("修改部门测试用例")
    def test_tc000052(self, inin_organiz):
        """
        当前已有部门,修改部门信息，传一个不存在的部门id
        :param inin_organiz: 环境初始化，创建销售部
        :return:
        """
        self.org_api = inin_organiz[0]
        self.edit_org = self.org_api.edit(_id="sda4545454", name="修改的部门")
        # 根据报错信息断言
        assert self.edit_org["error"]["code"] == 500

    @allure.story("部门-OrganizAPI-删除部门")
    @allure.title("删除部门测试用例")
    def test_tc000092(self, inin_organiz):
        """
        当前系统已有部门，删除一个id不存在的部门
        :param inin_organiz: 环境初始化，删除所有部门
        :return:
        """
        self.org_api = inin_organiz[0]
        orgs1 = self.org_api.list_all()
        self.org_api.delete("54543454544")
        orgs2 = self.org_api.list_all()
        assert orgs1 == orgs2


