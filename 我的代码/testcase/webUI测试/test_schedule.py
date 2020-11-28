#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:01
# @File : main_test.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from 我的代码.pylib.webUI.pageObjects.loginPage import LoginPage


def test_schedule():
    title = LoginPage().login('zhaoyun@test.com', '123456').driver.title
    print(title)



