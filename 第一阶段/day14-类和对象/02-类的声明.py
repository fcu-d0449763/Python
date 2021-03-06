# @Author   :xaidc
# @Time     :2018/9/6 9:20
# @File     :02-类的声明.py

"""
类：对拥有相同功能（方法）和相同属性的封装

封装效果：一个类中可以对多个功能进行封装（多个函数）；封装多个属性

1.类的声明格式
class 类名(父类列表)：
    类的说明文档
    类的内容

2.说明：
class:声明类的关键字
类名:标识符，不能是关键字。驼峰式命名（第一个单词首字母其他单词首字母都大写），首字母大写！！！，见名知义
    例如：Person,StudentSystem
(父类列表):这个部分可以省。这个是继承语法。
冒号：固定的
类的内容：包括类的方法和类的属性

3.类中的方法
方法：就是声明在类的函数
a.对象方法：对象方法需要通过对象来调用，对象.函数名()
直接写在；类中的方法，自带一个self参数

b.类方法:
c.静态方法:


4.创建对象
创建类的时候，系统会默认给我们创建这个类对应的构造方法
构造方法：类名() --->创建类对应的对象

"""
# 创建一个类
class Person:
    """人类 """
    def eat(self):
        print('人吃饭')
# 1.创建对象
p1 = Person() #创建Person类的对象，并且将对象的地址存到p1中
# 一个类可以有多个对象
p2 = Person()
# 只有在调用方法的时候才会产生新的对象
p3 = p2
print(id(p1),id(p2),id(p3))
#2. 调用对象方法
# 通过对象调用对象方法，默认参数self不需要传参。系统会自动传
p1.eat()
