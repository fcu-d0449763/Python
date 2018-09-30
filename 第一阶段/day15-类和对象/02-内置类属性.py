# @Author   :xaidc
# @Time     :2018/9/7 9:14
# @File     :02-内置类属性.py
"""
内置类属性就是魔法属性
魔法属性：属性名的前面和后面都有两个下划线
魔法方法：方法的前后都有两个下划线

"""
import datetime
class Person:
    """人类"""
    # 类的字段
    number = 61
    def __init__(self,name,age,height):
        # 对象的属性
        self.name = name
        self.age = age
        self.height = height
    # 对象方法
    def run(self):
        print('%s在跑步'%self.name)
    # 类方法
    @classmethod
    def show_number(cls):
        print('人类的数量为：%d亿'%cls.number)
    #静态方法
    @staticmethod
    def destory():
        print('人类在破坏环境！')



if __name__ == '__main__':
    p1 = Person('张三',28,170)
    # 1.__name__属性  ---_类的名字(是个字符串)
    name = Person.__name__
    print(name,type(name))
    # 2.__class__属性 ---获取对象对应类（是一个类）
    # 对象的属性
    # my_class是一个类，之前类能做的事他都能做
    my_class = p1.__class__
    p2 = my_class('小明',20,180)
    print(p2.name,my_class.__class__)

    # 3.__dict__属性 ---将对象和类的属性及其对应的值转换成键值对存到一个字典中
    print(p1.__dict__)

    # 4.__doc__属性 ---获取类的说明文档
    # 类的属性
    doc = Person.__doc__
    print(doc)

    # 5.__module__属性----获取类所在的模块对应的名字
    print(Person.__module__)
    print(datetime.datetime.__module__)

    # 6.__bases__属性 ---获取当前类的父亲
    # 类的属性
    print(Person.__bases__)