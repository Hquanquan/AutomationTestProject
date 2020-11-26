"""
@author: haiwen
@date: 2020/11/20
@file: conftest.py
"""
import pytest


# 创建销售部

# 创建数据环境-销售部
@pytest.fixture(scope='session', autouse=True)
def init_organiz(empty_organiz):
    org_api = empty_organiz
    sale_org = org_api.add('销售部')
    yield sale_org
    # 删除销售部
    org_api.delete(sale_org['_id'])
