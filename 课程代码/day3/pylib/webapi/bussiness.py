'''
@author: haiwen
@date: 2020/11/22
@file: bussiness.py
'''
from conf.env import top_parent
from pylib.webapi.common import BaseAPI

#部门
class OrganizAPI(BaseAPI):
    def add(self,name,parent=top_parent):
        return super().add(name=name,parent=parent)

    def edit(self,organization_id,name=None,parent=top_parent):
        return super().edit(organization_id,name=name,parent=parent)

    def delete_all(self):
        items = self.list_all()[1:]
        for item in items:
            self.delete(item['_id'])

#签约对象
class AccountsAPI(BaseAPI):
    pass

#合同类型
class ContractTypesAPI(BaseAPI):
    pass

#合同
class ContractsAPI(BaseAPI):
    pass



