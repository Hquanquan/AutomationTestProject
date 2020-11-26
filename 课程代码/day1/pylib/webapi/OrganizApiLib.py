"""
@author: haiwen
@date: 2020/11/20
@file: OrganizApiLib.py
"""
import requests
from 课程代码.day1.conf.env import host, global_email, global_psw, top_parent


# 部门API
class OrganizApi:
    def __init__(self, cookies):
        self.host = host
        self.path = '/api/v4/organizations'
        self.cookies = cookies
        self.space_id = self.cookies['X-Space-Id']  # 从cookies中获取spaceid

    def add(self, name, parent=top_parent):
        payload = {
            "name": name,
            "parent": parent,
            "sort_no": 100,
            "hidden": False,
            "space": self.space_id  # 公司ID全局唯一，每个管理员不同
        }
        resp = requests.post(f'{self.host}{self.path}', json=payload, cookies=self.cookies)
        return resp.json()['value'][0]  # 取出新增返回信息

    def list_all(self):
        resp = requests.get(f'{host}{self.path}', params={'spaceid': self.space_id}, cookies=self.cookies)
        return resp.json()['value']  # 信息部分在value字段

    def delete(self, organization_id):
        resp = requests.delete(f'{host}{self.path}/{organization_id}', cookies=self.cookies)
        return resp.json()

    def delete_all(self):
        # 只有删除单个部门的webapi
        # 先列出所有，再挨个删除
        orgs = self.list_all()[1:]  # 去掉第一个总公司ID，因为不能被删除
        for org in orgs:
            self.delete(org['_id'])
