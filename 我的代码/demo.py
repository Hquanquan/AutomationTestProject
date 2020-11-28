#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 11:24
# @File : demp.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import configparser

config = configparser.ConfigParser()
# 获取配置文件的路径
# file_path = "../../../conf/config.ini"
file_path = "conf/config.ini"
# 读取该文件所有内容
config.read(file_path)
# 读取浏览器类型信息,并打印日志
browserName = config.get("testServer", "URL")
print(browserName)