'''
@author: haiwen
@date: 2020/11/22
@file: main_test.py
'''
import pytest
import os

if __name__ == '__main__':
    # pytest.main(['testcase','-s','--alluredir=tmp/report'])
    #os.system('allure serve tmp/report')
    pytest.main(['testcase','-s','--alluredir=tmp/report'])
    os.system('allure serve tmp/report')