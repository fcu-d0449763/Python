# @Author   :xaidc
# @Time     :2018/9/6 16:50
# @File     :homework.py
"""
1.声明一个电脑类: 属性:品牌、颜色、内存    方法:打游戏、写代码、看视频
a.创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
b.通过attr相关方法去获取、修改、添加和删除它的属性
"""
'''
class Computer:
    def __init__(self,brand,color,memory):
        self.brand = brand
        self.color = color
        self.memory = memory
    def play_game(self):
        p1 = '这是打游戏方法'
        return p1
    def write_code(self):
        w1 = '这是写代码的方法'
        return w1
    def watch_video(self):
        w2 = '这是看视频方法'
        return w2

c1 = Computer('联想','黑色','8G')
print(c1.play_game())
print(c1.write_code())
print(c1.watch_vedeo())
# 获取属性
print(c1.brand)
print(c1.color)
print(c1.memory)
#修改属性
c1.brand = '华硕'
print(c1.brand)
#添加属性
c1.size = '八寸'
print(c1.size)
# 删除属性
del c1.size
# attr 查看属性
print(c1.__getattribute__('brand'))
# attr 修改属性
setattr(c1,'brand','神州')
print(c1.brand)
# attr 增加属性
setattr(c1,'size','九存')
# attr 删除属性
delattr(c1,'color')
'''
"""
2.声明一个人的类和狗的类：
狗的属性：名字，颜色，年龄，狗的方法：叫唤
人的属性：名字，年龄，狗 人的方法：遛狗
a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄
"""
'''
class Person:
    def __init__(self,name,age,dog):
        self.name = name
        self.age = age
        self.dog = dog
    def walk_the_dog(self,dog_name):
        print('%s遛%s'%(self.name,self.dog))


class Dog:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
    def bark(self):
        r = '汪汪汪'
        return r

d1 = Dog('大黄','黄色','2')
p1 = Person('小明','34',d1.name)
p1.walk_the_dog(d1.name)
'''
"""
3.声明一个矩形类：
属性：长，宽 方法：计算周长和面积
a.创建不同的矩形，并且打印其周长和面积
"""
'''
class Rect:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return (self.length+self.width)*2
r1 = Rect(2,3)
r2 = Rect(7,8)
x1 = r1.area()
x2 = r1.perimeter()
x3 = r2.area()
x4 = r2.perimeter()
print("r1的面积和周长分别是%d,%d"%(x1,x2))
print("r1的面积和周长分别是%d,%d"%(x3,x4))
'''
"""
4.创建一个学生类：
属性：姓名，年龄，学号  方法:答到，展示学生信息
创建一个班级类：
属性：学生，班级名 方法：添加学生，删除学生，点名

"""
'''
class Student:
    def __init__(self,name,age,num):
        self.name = name
        self.age = age
        self.num = num
    # def atr(self):

    # def show_information(self,p):
    #     p = Studen
    #     print("学生%s姓名是%s，年龄%s，学号%s"%(p,p.name))
students = []
class Class:

    def __init__(self,student,class_name):
        self.student = student
        self.class_name = class_name

    @classmethod
    def add_student(cls,name):
        # name1 = input("请输入名字：")
        age1 = input("请输入年龄：")
        num1 = input("请输入学号：")
        name = Student(name,age1,num1)
        students.append(name)
    @classmethod
    def del_student(cls):
        name = input("请输入要删除学生的姓名")
        for stu in students[:]:
            if stu == name:
                del stu
    # @classmethod
    # def call_the_roll(cls):
while True:
    print("1.添加学生")
    print("2.删除学生")
    print("3.点名")
    n = input("请输入（1-3）：")
    if n == '1':
        name = input("请输入名字：")
        Class.add_student(name)
    if n == '2':
        Class.del_student()
    print(students)
'''
# 5.写一个类，封装所有和数学运算相关的内容（包括常用功能和常用值，例如pi，e等）
import math
class Math1:
    def __init__(self):
        self.pi = math.pi
        self.e = math.e
    def sum(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def abs(self,num):
        if num >= 0:
            return num
        if num < 0:
            return -num
    def pow(self,num1,num2):
        return num1**num2
    def multiply(self,num1,num2):
        return num1*num2

