'''
@author: haiwen
@date: 2020/11/25
@file: bunsiness.py
'''
import time

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


class MainMenuPage(BasePage):
    def logout(self):
        self.click(self.avatar)
        self.click(self.logout_btn)
        return LoginPage()

    def to_schedule(self):
        self.click(self.schedule_link)
        # 进入日程界面了？
        return SchedulePage()


class HomePage(MainMenuPage):
    def get_title(self):
        return self.driver.title

    def get_schedule_list(self):
        schedule_list = self.multi_text(self.schedules)
        return schedule_list


class SchedulePage(MainMenuPage):
    def new_schedule(self, theme, target_name):
        # 点击新建
        self.click(self.new_btn)
        # 填写表格--输入主题
        self.input_text(self.summary_input, theme)
        # 点击分配用户
        self.click(self.selectUser_box)
        time.sleep(1)  # 稳定页面弹出框
        # 清除已经选择的用户
        self.click_multi(self.selected_users)
        # 选择目标用户
        self.select_target(self.target_users, target_name)
        # 点击确认
        self.click(self.confirm_btn)
        # 点击保存
        self.click(self.save_btn)
        # 返回当前页面
        return self
