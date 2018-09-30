# @Author   :xaidc
# @Time     :2018/9/6 15:59
# @File     :08-类的方法.py

"""
1.对象方法（实例方法）
声明的形式：直接声明在类中
特点：自带一个不需要主动传参的默认参数self，谁来调用指向谁
调用：通过对象来调用

2.类方法
声明的形式：声明方法前需要使用@classmethod
特点：自带一个默认参数cls，这个参数调用的时候不需要传值。系统自动给他传。谁调用就指向谁！始终指向当前类
调用：通过类来调用->类.类方法名（）

3.静态方法
声明形式：声明方法前需要使用@staticmethod说明
特点：没有默认的参数
调用：通过类来调用 -> 类.静态方法（）
"""
class Person:
    #类字段
    number = 100
    #声明一个对象方法
    def object_func(self):
        print('对象方法')
    # 声明一个类方法
    @classmethod
    def class_func(cls):
        #通过cls去使用类的字段
        print('cls:',cls.number)
        # 通过cls去创建对象
        tc = cls()
        tc.object_func()
        print('这是一个类方法')
    @staticmethod
    def static_func():
        print('这是一个静态方法')

c1 = Person()
c1.object_func()
print(Person.number)
# 调用类方法
Person.class_func()
# 调用静态方法
Person.static_func()
"""
4.遇到问题怎么来选择使用哪种方法：
a.大前提：只要实现方法的功能需要用到对象的属性，我们就使用对象方法。否则就使用静态方法或者类方法
b.你不使用对象方法的前提下，如果实现功能需要用到类的字段就使用类方法
c.实现功能既不需要对象的属性，又不需要类的字段就使用静态方法
注意：静态方法和类方法划分不用那么严格，静态方法能做的类方法可以做，反之亦然

"""
class Person:
#     类的字段，存储人类的数量
    number = 61
    @classmethod
    def shou_numer(cls):
        print('人类的数量是：%d亿'%cls.number)

    @staticmethod
    def show_numer2():
        print('人类的数量是：%d亿'%Person.number)






if __name__ == '__main__':
    pass