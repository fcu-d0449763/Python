# @Author   :xaidc
# @Time     :2018/9/6 14:24
# @File     :06-对象方法.py

"""
1.对象方法：
a.什么样的方法是对象方法：直接声明在类的函数默认是对象方法，有一个默认参数self
b.对象方法要通过对象来调用：对象.对象方法()
c.对象方法中默认参数self，不需要传参。因为在调用这个方法时，系统会自动将当前对象传给self
哪个对象调用的方法，self就指向谁

"""
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    # 声明了一个对象方法area
    #在这儿，self就是调用area方法的对象。对象能做的事情，self都可以做
    def area(self):
        return math.pi*self.radius**2

# 练习1：写一个矩形类，有属性长和宽,有两个功能，求面积和周长
class Rect:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return (self.length+self.width)*2




# 练习2：写一个班级类，班级里面有多个学生的成绩（一门），班级名，可以获取班级成绩的最高分
class Class1:
    def __init__(self,class_name,*grade):
        self.class_name = class_name
        self.grade = grade
    def max_grade(self):
        list1 = list(self.grade)
        return max(list1)
#  max（序列） ---->获取序列中元素的最大值
#  min（序列）----->获取序列中元素的最小值

if __name__ == '__main__':
    #创建了一个半径为3的圆的对象
    c1 = Circle(3)
    print(id(c1))
    print(c1.area())
    #创建一个半径是5的圆的对象
    c2 = Circle(5)
    print(c2.area())

    r1 = Rect(1, 2)
    print(r1.area())

    r2 = Rect(2, 3)
    print(r2.perimeter())

    c3 = Class1('python1806',23,45,67,34)
    print(c3.max_grade())