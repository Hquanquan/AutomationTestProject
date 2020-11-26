#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 9:25
# @File : commom.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from functools import wraps

import allure
import yaml


def read_yaml(filepath):
    """
    读取yaml文件数据，并以字典格式返回
    :return:
    """
    with open(filepath, encoding="utf-8") as f:
        # 读取yaml文件内容,赋值到content
        content = f.read()
        # 把content转化为字典格式
        data_json = yaml.safe_load(content)
        return data_json

class YAML:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_yaml(self):
        """
        读取yaml文件数据，并以字典格式返回
        :return:
        """
        with open(self.filepath, encoding="utf-8") as f:
            # 读取yaml文件内容,赋值到content
            content = f.read()
            # 把content转化为字典格式
            data_json = yaml.safe_load(content)
            return data_json

# 自定义的装饰器
def dynamic_report(target, target_tile=None):
    def decorate(fun):
        @wraps(fun)  # 保留测试方法原来的信息
        def warpper(*args, **kwargs):
            res = fun(*args, **kwargs)
            desc = kwargs[target]  # 从用例参数列表获取要表示的字段
            allure.dynamic.description('用例描述---%s' % desc)
            if target_tile:  # 如果指定了目标标题就从参数列表的数据自定义报告标题
                title = kwargs[target_tile]
                allure.dynamic.title(title)
            return res
        return warpper
    return decorate


if __name__ == '__main__':
    # text = read_yaml("../../conf/api_conf.yaml")

    yml = YAML("../../conf/api_conf.yaml")
    text = yml.read_yaml()
    print(text["BaseAPI"])
