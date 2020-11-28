'''
@author: haiwen
@date: 2020/11/22
@file: configer.py
'''
import yaml
def read_yml(path):
    with open(path,encoding='utf8') as f:
        content=f.read()
        return yaml.safe_load(content)


class DemoApi():
    def __init__(self):
        res=read_yml('../../conf/api_conf.yml')
        #获取当前类的class——name
        current_classname=self.__class__.__name__
        self.conf=res[current_classname]
        print(self.conf)

    def get_payload(self,name):
        return self.conf[name]

    #不知道要替换哪些参数
    def update_payload(self,api,**kwargs):
        payload=self.conf[api] #从配置文件中读取的模板
        #替换模板中的数据
        payload.update(kwargs)
        print(payload)

#哪个类继承baseapi，就用该类的类名做为key,同时conf文件中的配置项名称需要和继承的子类class同名

class OrganizAPI(DemoApi):
    pass

class ContractsAPI(DemoApi):
    pass

if __name__ == '__main__':
    #data={'sort_no':999,'age':18}
    #res=ContractsAPI()
    res=read_yml('../../conf/ele_conf.yml')
    print(res)
