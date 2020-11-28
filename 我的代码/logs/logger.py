#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 10:14
# @File : logger.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : logger日志类
import logging
import os

from 我的代码.pylib.utils.convertData import ConvertData


class Logger(object):

    def __init__(self, logger):
        """
        初始化
        :param logger:  logger对象被执行的对象类
        """
        # 创建一个logger对象
        self.logger = logging.getLogger(logger)
        # 设置日志模式为debug调试模式
        self.logger.setLevel(logging.DEBUG)

        # 设置时间格式
        time_format = ConvertData.current_time(time_formate="%Y%m%d%H%M%S", tager=False)
        # print(time_format)
        log_path = r"log/"
        # print(log_path)
        isExists = os.path.exists(log_path)
        # print(isExists)

        # 判断log文件夹是否被创建，为创建则进行创建
        if not isExists:
            try:
                # 创建这个路径的文件
                os.makedirs(log_path)
            except Exception as e:
                print("创建文件夹失败！原因：", e)
        # log日志的名称以时间来命名
        log_name = log_path + time_format + '.log'
        # 创建一个handler,用于写入日志文件，注意一定要指定编码格式encoding="utf-8"
        fh = logging.FileHandler(log_name, encoding="utf-8")
        fh.setLevel(logging.INFO)

        # 再创建一个hangler，用于输出日志到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 给logger添加hangler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    # 获取logger
    def getlog(self):
        return self.logger


