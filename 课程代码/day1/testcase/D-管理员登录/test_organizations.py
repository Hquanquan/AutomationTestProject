"""
@author: haiwen
@date: 2020/11/20
@file: test_organizations.py
"""
import pytest

from 课程代码.day1.pylib.webapi.OrganizApiLib import OrganizApi

class TestOrganizApi:

    @pytest.fixture()
    def before_tc000001(self, admin_login):
        self.cookies = admin_login
        self.org_api = OrganizApi(self.cookies)
        self.org_api.delete_all()
        yield
        self.org_api.delete(self.org["_id"])


    def test_tc000001(self, before_tc000001):
        # step1
        self.org = self.org_api.add('研发部门')
        # step2
        orgs = self.org_api.list_all()
        assert self.org in orgs  # 判断创建的信息是否包含在列表中




