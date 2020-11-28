'''
@author: haiwen
@date: 2020/11/23
@file: test_contract.py
'''
import allure
import pytest

from pylib.webapi.bussiness import ContractsAPI
from pylib.utlis.pulgins import ConvertData, dynamic_report


@pytest.fixture(scope='package')
def emtpy_contracts(admin_login):
    global contract_api
    contract_api = ContractsAPI(admin_login)
    contract_api.delete_all()
    yield
    contract_api.delete(contract['_id'])

@dynamic_report('name','amount')
@pytest.mark.parametrize('name,amount',ConvertData.get_param())
def test_tc003001(name,amount,emtpy_contracts,init_organiz,
                  init_contract_type,init_accounts):
    global contract
    #step1
    contract=contract_api.add(name=name,amount=amount,
                    company_id=init_organiz['_id'],
                     contract_type=init_contract_type['_id'],
                     othercompany=init_accounts['_id'],
                    create_date=ConvertData.current_time())

    #step2
    contracts=contract_api.list_all()
    assert contract in contracts


