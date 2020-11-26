#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 10:17
# @File : tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import os


def get_rootPath():
    """获取项目根目录"""
    root_path = os.path.abspath(os.path.dirname(__file__)).split('自动化项目实战')[0] + "自动化项目实战\我的代码\\"
    return root_path


if __name__ == '__main__':
    print(get_rootPath())
