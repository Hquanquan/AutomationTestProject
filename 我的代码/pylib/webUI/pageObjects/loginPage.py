#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 17:06
# @File : loginPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from 我的代码.pylib.webUI.pageObjects.basePage import BasePage
from 我的代码.pylib.webUI.pageObjects.homePage import HomePage


class LoginPage(BasePage):
    def login(self, email, psw):
        self.driver.get('http://devops.sqtest.online:6003/')
        self.input_text(self.email_input, email)
        self.input_text(self.psw_input, psw)
        #
        self.click(self.login_btn)
        return self


