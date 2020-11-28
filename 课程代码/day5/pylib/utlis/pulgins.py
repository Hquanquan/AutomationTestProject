'''
@author: haiwen
@date: 2020/11/23
@file: pulgins.py
'''
import datetime
import sys
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


import logging


def logger(level='info'):
    def decorate(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            res = fun(*args, **kwargs)
            if level.upper() in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                log = getattr(logging.getLogger('WebUI'), level.lower())
                if len(args)>1:
                    content = '%s element with locator: %s, text: %s' % (fun.__name__, args[0], args[1])
                else:
                    content = '%s element with locator: %s' % (fun.__name__, args[0])
                log(content)
            return res
        return wrapper
    return decorate


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
log_conf={
    'stream':sys.stdout,
    'level':logging.DEBUG,
    'datefmt':DATE_FORMAT,
    'format':LOG_FORMAT,
}

# logging.basicConfig(**log_conf)

@logger()
def click(locator):
    pass


@logger()
def input_text(locator, text):
    pass


if __name__ == '__main__':
    # res=ConvertData.get_param('../../case_data/contracts_data.yml')
    # print(res)
    click(['id', 'email'])
    input_text(['id', 'email'], 'hello world')
