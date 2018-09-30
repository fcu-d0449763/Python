# @Author   :xaidc
# @Time     :2018/9/7 14:11
# @File     :06-继承.py
"""
python 中可以继承，并且支持多继承
程序中的继承：就是让子类直接拥有父类的属性和方法（继承后父类中的内容不会因为被继承而减少）
1.继承的语法
class 子类(父类)：
    类的内容

注意：如果声明的时候没有写继承，那么这个类会自动继承python的基类，object；相当于class 类名（object）：
    python中所有的类都是直接或者间接的继承自object

2.能继承哪些东西
a 所有的属性和方法都能继承
b __slots__的值不会继承，但是会影响子类对象的__dict__属性，不能获取到父类继承下来的属性

"""
class Person:
    """人类"""
    number = 61
    # __slots__ = ('name','age')

#     对象属性
    def __init__(self,name = '张三',age = 18,__height = 123):
        self.name = name
        self.age = age
        self.height = __height

#     对象方法
    def show_message(self):
        print('姓名：%s 年龄：%d'%(self.name,self.age))

#     类方法
    @classmethod
    def show_number(cls):
        print('人类的数量是：%d'%cls.number)

#     静态方法
    @staticmethod
    def complaint():
        print('人类殴打小动物')
class Student(Person):
    """学生类"""
    pass

# 创建Person类的对象

stu1 = Student()
print(Student.number)
stu1.name = '李四'
print(stu1.name)
stu1.show_message()
Student.show_number()
Student.complaint()
stu1.sex = 'boy'
print(stu1.__dict__)


if __name__ == '__main__':
    pass