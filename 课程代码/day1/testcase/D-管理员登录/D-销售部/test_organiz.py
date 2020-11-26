"""
@author: haiwen
@date: 2020/11/20
@file: test_organiz.py
"""
import pytest

@pytest.fixture()
def after_tc000002(init_organiz):
    org_api = init_organiz
    yield org_api
    org_api.delete(org["_id"])

def test_tc000002(after_tc000002):
    global org
    org_api = after_tc000002
    # step1
    org = org_api.add('测试部门')
    # step2
    orgs = org_api.list_all()
    assert org in orgs  # 判断创建的信息是否包含在列表中

