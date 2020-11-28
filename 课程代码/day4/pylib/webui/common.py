"""
@author: haiwen
@date: 2020/11/25
@file: common.py
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pylib.utlis.configer import read_yml


class WebdriverCreater:
    # 实现单例模式
    # new方法--通过cls调用，调用new方法后生成对象
    def __new__(cls, *args, **kwargs):
        # 判断该cls是否有对应的实例
        if hasattr(cls, '_instance'):
            return cls._instance
        cls._instance = object.__new__(cls)  # 创建对象
        return cls._instance

    # 定义获取webdriver定方法
    def get_browser(self):
        # 判断当前对象是否有driver属性，如果有直接返回，如果没有造一个再返回
        if hasattr(self, 'driver'):
            return self.driver
        self.driver = webdriver.Chrome(r'E:\Python\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(10)
        return self.driver


class BasePage:
    def __init__(self, conf_path='conf/ele_conf.yml'):
        self.driver = WebdriverCreater().get_browser()  # 打开浏览器
        # 使用当前类名作为元素配置的关键字
        current_class = self.__class__.__name__
        eles = read_yml(conf_path)[current_class]
        # eles的key作为属性名称，value作为属性值
        for key in eles:
            # self.__setattr__(属性名称(str)，属性值) 动态生成对象属性
            self.__setattr__(key, eles[key])

    def input_text(self, locator, text):
        self.click(locator)  # 点一下再输入
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator[0], locator[1])))
        ele.click()

    def close_browser(self):
        self.driver.quit()
        self.driver = None  # 置空driver对象


if __name__ == '__main__':
    w1 = WebdriverCreater()
    w2 = WebdriverCreater()
    w1.get_browser()
    w2.get_browser()
