"""
@author: haiwen
@date: 2020/11/20
@file: test_organizations.py
"""
import pytest


@pytest.fixture()
def after_tc000001(empty_organiz):
    # 初始化动作
    org_api = empty_organiz
    # 清除用例tc000001产生的数据
    yield org_api  # yield之后如果没有代码，作用和return一样
    # 清除动作
    org_api.delete(org['_id'])


# 每一层清除自身产生的数据
def test_tc000001(after_tc000001):
    global org
    org_api = after_tc000001
    # step1
    org = org_api.add('研发部门')
    # step2
    orgs = org_api.list_all()
    assert org in orgs  # 判断创建的信息是否包含在列表中


@pytest.fixture()
def before_tc000091(empty_organiz):
    org_api = empty_organiz
    glory_org = org_api.add('荣耀')
    yield org_api, glory_org


def test_tc000091(before_tc000091):
    org_api = before_tc000091[0]
    glory_org = before_tc000091[1]
    # step1
    org_api.delete(glory_org['_id'])
    # step2  返回结果公司分部列表为空
    res = org_api.list_all()[1:]  # 过滤掉总公司
    assert res == []
