#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 15:28
# @File : convertData.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import datetime

from 我的代码.pylib.utils.commom import read_yaml


class ConvertData:

    @staticmethod
    def current_time(time_formate="%Y-%m-%dT%H:%M:%S.%f"):
        """
        获取当前时间，转换为指定的字符串格式返回
        :param time_formate: 格式
        :return:
        """
        dt = datetime.datetime.now()
        current_time = dt.strftime(time_formate)
        return current_time[:-3] + "Z"

    @staticmethod
    def get_param(path='casedata/contracts_data.yml'):
        data = read_yaml(path)
        values = [data[key] for key in data]
        res = []
        for i in range(len(values[0])):
            ele = []
            for k in range(len(values)):
                ele.append(values[k][i])
            res.append(ele)
        return res


if __name__ == '__main__':
    param = ConvertData.get_param()
    print(param)
