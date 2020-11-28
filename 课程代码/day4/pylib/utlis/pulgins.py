"""
@author: haiwen
@date: 2020/11/23
@file: pulgins.py
"""
import datetime
from functools import wraps

import allure

from pylib.utlis.configer import read_yml


class ConvertData:
    @staticmethod
    def current_time(time_formate='%Y-%m-%dT%H:%M:%S.%f'):
        # 获取当前时间，并且转化为对应的格式
        dt = datetime.datetime.now()
        cur_time = dt.strftime(time_formate)
        return cur_time[:-3] + 'Z'

    @staticmethod
    def get_param(path='case_data/contracts_data.yml'):
        test_data = read_yml(path)
        # 转化成[(name1,amount1),(name2,amout2),....]
        # 1.取出value列表
        values = [test_data[key] for key in test_data]
        #
        res = []
        for i in range(len(values[0])):
            ele = []  # 表示元素对，元组不能修改，只能用List代替
            for k in range(len(values)):
                ele.append(values[k][i])
            res.append(ele)  # 收集元素
        return res


def before_after(before, after):
    def decorate(fun):
        @wraps(fun)
        def warpper(*args, **kwargs):
            print(before)
            res = fun(*args, **kwargs)
            print(after)
            return res

        return warpper

    return decorate


@before_after('周末了', '约女朋友出去玩')
def test_func(name='小明'):
    print(name + '今天心情很好')


# 计算方法执行时间的装饰器
def count_fun_exec_time():
    pass


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
    # res=ConvertData.get_param('../../case_data/contracts_data.yml')
    # print(res)
    print(test_func.__name__)
