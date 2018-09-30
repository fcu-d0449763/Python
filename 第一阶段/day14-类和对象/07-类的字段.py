# @Author   :xaidc
# @Time     :2018/9/6 15:40
# @File     :07-类的字段.py
"""
类的属性叫类的字段
a.什么是类的字段
类的字段就是声明在类的里面，方法的外面的变量
b.什么样的属性声明成类的字段：
属于类的，对于这个类的所有的对象来说其值是共有的
c.怎么使用：
通过类来使用：类.字段
"""
class Person:
    #这个number就是类的字段
    number = 61

# 练习：写一个球类，用一个属性来保存这个类的创建对象的个数
class Ball:
    count = 0
    # 每次创建球的对象都会调用init方法，所以init方法调用的次数就是Ball创建的对象的个数
    def __init__(self):
        Ball.count += 1
ball1 = Ball()
ball2 = Ball()
print(Ball.count)

if __name__ == '__main__':
    # 通过类获取类的字段的值
    print(Person.number)
    Person.number = 70
    print(Person.number)