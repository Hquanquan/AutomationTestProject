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
        # 浏览器加载页面响应超时时间
        self.driver.set_page_load_timeout(60)
        # js执行加载超时时间
        self.driver.set_script_timeout(60)
        self.driver.implicitly_wait(10)
        return self.driver


class BasePage:
    def __init__(self, conf_path='conf/ele_conf.yml'):
        self.driver = WebdriverCreater().get_browser()  # 打开浏览器
        self.__init_eles(conf_path)

    def __init_eles(self, conf_path):
        # 使用当前页面继承的所有页面类作为元素配置项,去掉basepage和object
        class_names = [m.__name__ for m in self.__class__.mro()][:-2]
        for class_name in class_names:
            eles = read_yml(conf_path)[class_name]
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

    # 实现点击多个元素
    def click_multi(self, locators):
        eles = self.driver.find_elements(*locators)
        for ele in eles:
            ele.click()

    # 选择目标元素
    def select_target(self, locators, target):
        eles = self.driver.find_elements(*locators)
        for ele in eles:
            # 通过元素文本判断是否为目标元素
            if ele.text == target:
                ele.click()
                print('找到目标元素')
                return
        print('目标元素未找到')

    # 获取多个元素文本
    def multi_text(self, locators):
        eles = self.driver.find_elements(*locators)
        return [ele.text for ele in eles]

    # 清除文本
    def clear_text(self, locator):
        # 如果操作元素的时候，元素发生变化就要重新获取，否则就会触发stale-element refrence exception
        # 先点击
        self.driver.find_element(*locator).click()
        # 再清除文本
        self.driver.find_element(*locator).clear()

    def close_browser(self):
        self.driver.quit()
        self.driver = None  # 置空driver对象
