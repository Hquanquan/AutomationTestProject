"""
@author: haiwen
@date: 2020/11/22
@file: bussiness.py
"""
from pylib.webapi.common import BaseAPI


# 部门
class OrganizAPI(BaseAPI):
    def __init__(self, cookies):
        super().__init__(cookies)
        # 获取topparent_id
        top_parent = self.list_all()[0]
        self.top_parent_id = top_parent['_id']

    def add(self, name, parent=None):
        # 如果没有传parent参数就用self_topprent_id
        if not parent:
            parent_id = self.top_parent_id
        else:
            parent_id = parent
        return super().add(name=name, parent=parent_id)

    def edit(self, organization_id, name=None, parent=None):
        if not parent:
            parent_id = self.top_parent_id
        else:
            parent_id = parent
        return super().edit(organization_id, name=name, parent=parent_id)

    def delete_all(self):
        items = self.list_all()[1:]
        for item in items:
            self.delete(item['_id'])


# 签约对象
class AccountsAPI(BaseAPI):
    pass


# 合同类型
class ContractTypesAPI(BaseAPI):
    pass


# 合同
class ContractsAPI(BaseAPI):
    pass
