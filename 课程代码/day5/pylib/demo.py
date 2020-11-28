"""
@author: haiwen
@date: 2020/11/27
@file: demo.py
"""


class Base:
    def __init__(self):
        pass

    def get_class_name(self):
        return self.__class__.__name__

    # 只能获取上一层
    def get_parents_name(self):
        bases = self.__class__.__bases__
        return [base.__name__ for base in bases]

    # 获取完整的继承树
    def get_ancestors_name(self):
        ancestors = self.__class__.mro()
        return [ancestor.__name__ for ancestor in ancestors]


class Father(Base):
    pass


class Mother(Base):
    pass


class Child(Father, Mother):
    pass


class Sub(Child):
    pass


if __name__ == '__main__':
    print(Sub().get_class_name())
    print(Sub().get_parents_name())
    print(Sub().get_ancestors_name())
