"""
@author: haiwen
@date: 2020/11/25
@file: test_schedule.py
"""
import pytest

from pylib.webui.bunsiness import LoginPage
from conf.env import global_email, global_psw


@pytest.fixture(scope='package')
def before_schedule_test():
    login_page = LoginPage()
    yield login_page
    login_page.close_browser()


@pytest.mark.parametrize('theme', ['军事会议', '年会', '分赏'])
def test_schedule(theme, before_schedule_test):
    login_page = before_schedule_test
    # 登录进入到日程界面
    schedule_page = login_page.login(global_email, global_psw).to_schedule()
    # 创建日程，指派用户，退出登录，并用指派用户登录主页获取日程信息
    schedule_list = schedule_page.new_schedule(theme, '赵云').logout().login('zhaoyun@test.com',
                                                                           '123456').get_schedule_list()
    assert theme in schedule_list
    # 当前用户退出登录
    schedule_page.logout()

    # 退出，并用被指定任务的用户登录
