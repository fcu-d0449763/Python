# @Author   :xaidc
# @Time     :2018/9/7 20:08
# @File     :homework4.py

# 3.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
class Person:
    number = 0
    def __init__(self,num):
        self.num = num
        Person.number += 1
    @classmethod
    def numbers(cls):
        return cls.number

p1 = Person(2)
P2 = Person(1)
P3 = Person(2)
print('对象个数是%d个'%Person.numbers())