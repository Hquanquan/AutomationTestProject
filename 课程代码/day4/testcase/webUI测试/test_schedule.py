'''
@author: haiwen
@date: 2020/11/25
@file: test_schedule.py
'''
from pylib.webui.bunsiness import LoginPage


def test_schedule():
    title = LoginPage().login('zhaoyun@test.com', '123456').get_title()



