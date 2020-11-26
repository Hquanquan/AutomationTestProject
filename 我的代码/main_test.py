#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:01
# @File : main_test.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import os

import pytest

if __name__ == '__main__':
    # pytest.main(["-s"])
    # pytest.main(["-s", "-k test_contractType.py"])

    for one in os.listdir('report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'report/tmp/{one}')

    pytest.main(['testcase', '-s', '--alluredir=report/tmp'])
    os.system('allure serve report/tmp')


