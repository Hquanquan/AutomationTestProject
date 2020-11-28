"""
@author: haiwen
@date: 2020/11/20
@file: common.py
"""
import requests
from conf.env import host, global_psw, global_email
from pylib.utlis.configer import read_yml


def login(email, psw):
    path = '/accounts/password/authenticate'
    payload = {"user": {"email": email},
               "password": psw,
               "code": "", "locale": "zhcn"}
    resp = requests.post(f'{host}{path}', json=payload)
    # 登录需要返回什么？获取鉴权信息--cookies
    return resp.cookies


# API特点：1.rest风格，同API  URL相同，数据都是json格式
class BaseAPI:
    def __init__(self, cookies):
        api_template = read_yml('conf/api_conf.yml')  # 注意文件的相对路径，和导库路径起点相同即可
        current_classname = self.__class__.__name__
        self.conf = api_template[current_classname]
        self.host = host
        self.path = self.conf['path']
        self.cookies = cookies
        self.space_id = self.cookies['X-Space-Id']

    def add(self, **kwargs):
        payload = self.conf['add']
        kwargs['space'] = self.space_id  # 同步一下spaceid
        payload.update(kwargs)  # 更新参数内容
        resp = requests.post(f'{self.host}{self.path}', json=payload, cookies=self.cookies)
        return resp.json()['value'][0]  # 取出新增返回信息

    def edit(self, _id, **kwargs):
        payload = self.conf['edit']
        kwargs['space'] = self.space_id
        payload.update(kwargs)
        # 将数据嵌套在$set中
        data = {}
        data['$set'] = payload
        resp = requests.put(f'{host}{self.path}/{_id}', json=data, cookies=self.cookies)
        return resp.json()

    def list_all(self):
        resp = requests.get(f'{host}{self.path}', cookies=self.cookies)
        return resp.json()['value']  # 信息部分在value字段

    def delete(self, _id):
        resp = requests.delete(f'{host}{self.path}/{_id}', cookies=self.cookies)
        return resp.json()

    def delete_all(self):
        items = self.list_all()
        for item in items:
            self.delete(item['_id'])
