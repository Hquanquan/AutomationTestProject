#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 15:36
# @File : basePage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : page页面基类，封装底层方法，用于被其他的页面类继承
from selenium.webdriver.support.wait import WebDriverWait

from 我的代码.conf.env import email, password
from 我的代码.logs.logger import Logger
from 我的代码.pylib.utils.commom import read_yaml
from 我的代码.pylib.webUI.commom.driver import Driver
from selenium.webdriver.support import expected_conditions as EC

# 声明一个Logger实例化对象 logger,用于记录日志

logger = Logger(logger="BasePage").getlog()
class BasePage:
    """
    BasePage 类，所有页面的基础类，所有的页面类都要继承该类
    """
    # 初始化 driver 对象
    def __init__(self, conf_path='conf/ele_conf.yml'):
        """
        初始化 driver 对象
        """
        logger.info("\n================")
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver()
        # # 登录
        # self.__login()
        # 使用当前类名作为元素配置的关键字
        current_class = self.__class__.__name__
        eles = read_yaml(conf_path)[current_class]
        # 如果有返回数据才进行动态赋值
        if eles:
            # eles的key作为属性名称，value作为属性值
            for key in eles:
                # self.__setattr__(属性名称(str)，属性值) 动态生成对象属性
                self.__setattr__(key, eles[key])


    # 通过登录页面进行登录,这个登录方法为私有方法，不可继承
    def __login(self):
        """
       私有方法，只能在类里边使用
       类外部无法使用，子类不能继承
       此函数解决登录问题
       :return:
        """
        # 找到用户输入框，输入用户账号
        self.driver.find_element_by_id("email").send_keys(email)
        # 找到密码输入框，输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        # 找到【下一步】并点击
        self.driver.find_element_by_css_selector(".MuiButton-containedPrimary span.MuiButton-label").click()

    def input_text(self, locator, text):
        logger.info(f"输入框输入了:{text}")
        self.click(locator)  # 点一下再输入
        self.driver.find_element(*locator).send_keys(text)


    def click(self, locator):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator[0], locator[1])))
        ele.click()
        logger.info("点击了")




