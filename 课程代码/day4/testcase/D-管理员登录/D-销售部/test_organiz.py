'''
@author: haiwen
@date: 2020/11/20
@file: test_organiz.py
'''
import pytest

@pytest.fixture()
def after_tc000002(empty_organiz):
    org_api = empty_organiz
    yield org_api
    org_api.delete(org['_id'])

def test_tc000002(after_tc000002):
    global org
    org_api=after_tc000002
    # step1
    org = org_api.add('测试部门')
    # step2
    orgs = org_api.list_all()
    assert org in orgs  # 判断创建的信息是否包含在列表中

@pytest.fixture()
def before_tc000051(empty_organiz):
    org_api=empty_organiz
    test_org=org_api.add('产品部门')
    yield org_api,test_org
    org_api.delete(test_org['_id'])

def test_tc000051(before_tc000051):
    org_api=before_tc000051[0]   #API
    test_org=before_tc000051[1]  #部门数据
    #修改部门名称，不能修改数据环境中的数据
    org_api.edit(test_org['_id'],'质量部门')
    orgs=org_api.list_all()
    #判断产品部门成功被修改成质量部门
    for org in orgs:
        #找到产品部门的ID
        if org['_id']==test_org['_id']:
            #判断该名称是否改为质量部门
            assert org['name']=='质量部门'
            break


def test_tc000052(empty_organiz):
    org_api=empty_organiz
    res=org_api.edit('lsdfiuo342432',name='hahahahah')
    print(res)
    assert res['error']['code']==500


def test_tc000092(empty_organiz):
    org_api = empty_organiz
    #step1
    orgs1=org_api.list_all()
    org_api.delete('1312312312')
    #step2--返回结果公司分部列表没有变动
    orgs2=org_api.list_all()
    assert orgs1 == orgs2
