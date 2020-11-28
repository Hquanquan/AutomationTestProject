#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 15:40
# @File : driver.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 驱动类，负责生成driver对象
import configparser

from selenium import webdriver

from 我的代码.conf.env import email, password


class Driver:
    # 初始化driver为None
    driver = None

    @classmethod
    def get_driver(cls):
        """
        获取浏览器驱动对象
        只有第一次调用本函数会创建浏览器，然后返回浏览器驱动对象
        第二次及以后都会直接返回浏览器驱动对象，不会重复创建
        """
        # 1、读取配置文件的信息，打开相应的浏览器
        # 实例化一个 configparser 对象 config
        config = configparser.ConfigParser()
        # 获取配置文件的路径
        # file_path = "../../../conf/config.ini"
        file_path = "conf/config.ini"
        # 读取该文件所有内容
        config.read(file_path, encoding="utf-8")
        # 读取浏览器类型信息,并打印日志
        browserName = config.get("browserType", "browserName")
        # logger.info("You had select %s browser!" % browserName)
        # 读取driver驱动路径信息
        driverPath = config.get("browserType", "driverPath")
        # logger.info("You had select %s " % driverPath)
        # 读取URl地址信息,并打印日志
        url = config.get("testServer", 'URL')
        # logger.info("The test server url is %s" % url)

        # 2、根据配置文件打开对应的浏览器和网站

        # dirver 如果为None 就读取创建driver
        if cls.driver is None:
            if browserName == "Chrome":
                cls.driver = webdriver.Chrome(driverPath)
                # logger.info('Starting Chorme browser!')
            elif browserName == "Firefox":
                # firefox火狐浏览器的驱动已安装在浏览器上，直接调用即可
                cls.driver = webdriver.Firefox()
                # logger.info('Starting Firefox browser!')
            elif browserName == "IE":
                cls.driver = webdriver.Ie(driverPath)
                # logger.info('Starting IE browser!')
            else:
                print("未配置此浏览器驱动")
                # logger.info("未配置此浏览器驱动:%s" % browserName)
                return
        # 利用获取到的briver 打开浏览器，访问url地址,使用try 语句
        try:
            # 窗口最大化
            cls.driver.maximize_window()
            cls.driver.get(url)
            # logger.info("Open url %s " % url)
            # 等待10秒
            cls.driver.implicitly_wait(10)
            # logger.info("Set implicitly wait 10")

            # 这里可以登录，进入系统首页再返回driver对象
            # cls.__login()

            # 返回driver实例化对象
            return cls.driver
        except Exception as e:
            print(e)
            # logger.info(e)

    # 通过登录页面进行登录
    @classmethod
    def __login(cls):
        """
       私有方法，只能在类里边使用
       类外部无法使用，子类不能继承
       此函数解决登录问题
       :return:
        """
        # 找到用户输入框，输入用户账号
        cls.driver.find_element_by_id("email").send_keys(email)
        # 找到密码输入框，输入密码
        cls.driver.find_element_by_id("password").send_keys(password)
        # 找到【下一步】并点击
        cls.driver.find_element_by_css_selector(".MuiButton-containedPrimary span.MuiButton-label").click()




if __name__ == '__main__':
    driver = Driver.get_driver()



