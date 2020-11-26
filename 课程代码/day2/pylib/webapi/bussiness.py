"""
@author: haiwen
@date: 2020/11/22
@file: bussiness.py
"""
from 课程代码.day2.conf.env import top_parent
from 课程代码.day2.pylib.webapi.common import BaseAPI


class OrganizAPI(BaseAPI):
    def add(self, name, parent=top_parent):
        return super().add(name=name, parent=parent)

    def edit(self, organization_id, name=None, parent=top_parent):
        return super().edit(organization_id, name=name, parent=parent)

    def delete_all(self):
        items = self.list_all()[1:]
        for item in items:
            self.delete(item['_id'])
