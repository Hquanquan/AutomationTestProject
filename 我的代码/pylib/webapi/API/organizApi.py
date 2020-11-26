#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 21:09
# @File : organizAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 部门管理API类

import requests

from 我的代码.conf.env import HOST, parent, email, password

# from 我的代码.pylib.webapi.user import User
from 我的代码.pylib.webapi.user import User


class OrganizAPI:

    def __init__(self, cookies):
        self.cookies = cookies
        self.space_id = self.cookies['X-Space-Id']  # 从cookies中获取spaceid
        self.host = HOST
        self.path = "/api/v4/organizations/"
        self.parent = parent

    def add(self, name, parent=None):
        """
        添加部门
        :param name: 部门名称
        :param parent: 部门上级id
        :param spaceid: 空间ID
        :param sort_no: 排序，默认100
        :return:
        """
        data = {
            "name": name,
            "parent": "parent",
            "sort_no": 100,
            "hidden": False,
            "space": self.space_id
        }

        if parent:
            data["parent"] = parent
        else:
            data["parent"] = self.parent

        payload = data
        url = f"{self.host}{self.path}"
        resp = requests.post(url, json=payload, cookies=self.cookies)
        return resp.json()["value"][0]

    def edit(self, organization_id, name):
        kwargs = {
            "name": name,
            "parent": parent,
            "sort_no": 100,
            "hidden": False,
            "space": self.space_id
        }
        data = {"$set": kwargs}
        payload = data
        url = f"{self.host}{self.path}{organization_id}"
        resp = requests.put(url, json=payload, cookies=self.cookies)
        return resp.json()

    def list_all(self):
        """
        列出部门
        :return:
        """
        payload = {"spaceid": self.space_id}
        url = f"{self.host}{self.path}"
        resp = requests.get(url, json=payload, cookies=self.cookies)
        return resp.json()["value"]

    def delete(self, organization_id):
        """
        删除单个部门
        :return:
        """
        url = f"{self.host}{self.path}{organization_id}"
        resp = requests.delete(url, cookies=self.cookies)
        return resp.json()

    def delete_all(self):
        orgs = self.list_all()[1:]  # 去掉第一个总公司ID，因为不能被删除
        for org in orgs:
            self.delete(org["_id"])


if __name__ == '__main__':
    cookies = User(email, password).login()
    org_api = OrganizAPI(cookies)
    new_org = org_api.add("测试部")
    print(type(new_org))
    org_api.edit(new_org["_id"], "测试开发部")
    org_api.delete(new_org["_id"])
    org_api.delete_all()
    orgs = org_api.list_all()
    for i in orgs:
        print(i)

