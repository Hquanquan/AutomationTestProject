"""
@author: haiwen
@date: 2020/11/25
@file: bunsiness.py
"""
from pylib.utlis.configer import read_yml
from pylib.webui.common import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    # 登录操作
    def login(self, email, psw):
        self.driver.get('http://devops.sqtest.online:6003/')
        self.input_text(self.email_input, email)
        self.input_text(self.psw_input, psw)
        #
        self.click(self.login_btn)
        return HomePage()  # 登录之后进入主页


class HomePage(BasePage):
    def get_title(self):
        return self.driver.title

    def to_schedule(self):
        self.click(self.schedule_link)
        # 进入日程界面了？
        return SchedulePage()


class SchedulePage(BasePage):
    def new_schedule(self, name, to_user):
        # 实现剩余的新建日程操作
        pass
