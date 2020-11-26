#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 21:37
# @File : baseApi.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : api基类，实现基本的CRUD增删改查功能，用于被业务api类继承
import os
import pprint
from json import JSONDecodeError

import requests

from 我的代码.conf.env import email, password, HOST
from 我的代码.pylib.utils.tools import get_rootPath
from 我的代码.pylib.webapi.user import User
from 我的代码.pylib.utils.commom import read_yaml


class BaseAPI:

    def __init__(self, cookies):
        self.cookies = cookies
        # cookies 里包含有spaceid
        self.space_id = self.cookies['X-Space-Id']
        self.host = HOST
        # 获取当前类的类名,便于根据类名获取yaml文件里的模板数据
        current_className = self.__class__.__name__

        # 两种方式获取配置文件的路径：1、绝对路径 2、相对路径
        rootPath = get_rootPath()
        path = rf"{rootPath}conf\api_conf.yaml"
        # path = "conf/api_conf.yaml"
        # 获取yaml文件数据
        api_template = read_yaml(path)
        # 根据当前类名获取yaml文件里的模板数据
        self.conf = api_template[current_className]
        self.path = self.conf["path"]

    def add(self, **kwargs):
        data = self.conf["add"]
        kwargs["space"] = self.space_id
        data.update(kwargs)
        payload = data
        url = self.host + self.path
        resp = requests.post(url, json=payload, cookies=self.cookies)
        return resp.json()["value"][0]

    def edit(self, _id, **kwargs):
        # 读取配置文件：edit 的内容
        data = self.conf["edit"]
        # 更新data的数据
        data.update(kwargs)
        data["space"] = self.space_id
        # 修改请求参数放到$set中
        payload = {"$set": data}
        url = self.host + self.path + "/" + _id
        resp = requests.put(url, json=payload, cookies=self.cookies)
        try:
            res = resp.json()
            return res
        except JSONDecodeError:
            return {}

    def list_all(self):
        url = self.host + self.path
        resp = requests.get(url, cookies=self.cookies)
        return resp.json()["value"]

    def delete(self, _id):
        url = self.host + self.path + "/" + _id
        resp = requests.delete(url, cookies=self.cookies)
        return resp.json()

    def delete_all(self):
        items = self.list_all()
        for item in items:
            self.delete(item['_id'])


if __name__ == '__main__':
    mycookies = User(email, password).login()
    base_api = BaseAPI(mycookies)
    pprint.pprint(base_api.conf)


