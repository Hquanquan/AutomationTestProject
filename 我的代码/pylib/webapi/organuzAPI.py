#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 11:35
# @File : organuzApi.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 部门管理API类，实现CRUD增删改查功能
import pprint

from 我的代码.conf.env import email, password
from 我的代码.pylib.webapi.baseApi import BaseAPI
from 我的代码.pylib.webapi.user import User


class OrganizAPI(BaseAPI):

    def __init__(self, cookies):
        super().__init__(cookies)
        # 设置topid
        self.parent_id = self._top_parent()

    # 获取总公司的ID
    def _top_parent(self):
        parent = self.list_all()[0]
        return parent['_id']

    def add(self, **kwargs):
        # 判断用户是否指定parentid
        if not kwargs.get('parent'):  # 如果没有传parentid,就用总公司的ID
            kwargs['parent'] = self.parent_id
        return super().add(**kwargs)

    def edit(self, _id, **kwargs):
        # 判断用户是否指定parentid
        if not kwargs.get('parent'):  # 如果没有传parentid,就用总公司的ID
            kwargs['parent'] = self.parent_id
        return super().edit(_id, **kwargs)

    def delete_all(self):
        # 列出所有部门，不包括总公司部门
        orgs = self.list_all()[1:]
        for org in orgs:
            self.delete(org['_id'])



if __name__ == '__main__':
    """
    mycookies = User(email, password).login()
    org = OrganizAPI(mycookies)
    new_org = org.add(name="背锅部")
    orgs = org.list_all()
    for i in orgs:
        pprint.pprint(i)
        print("=" * 100)
    text = org.edit(new_org["_id"], name="产品背锅部")
    print(text)
    print("******** 操作后的列表 ***********")
    orgs = org.list_all()[1:]
    for i in orgs:
        pprint.pprint(i)
        print("=" * 100)
    org.delete_all()
    """

    mycookies = User(email, password).login()
    org_api = OrganizAPI(mycookies)
    pprint.pprint(org_api.conf)


