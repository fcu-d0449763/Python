# @Author   :xaidc
# @Time     :2018/9/6 20:05
# @File     :homework1.py

"""
4.创建一个学生类：
属性：姓名，年龄，学号  方法:答到，展示学生信息
创建一个班级类：
属性：学生，班级名 方法：添加学生，删除学生，点名

"""
class Student():
    def __init__(self,name,age,num):
        self.name = name
        self.age = age
        self.num = num

    def show_information(self,p):
        return p.name,p.age,p.num

    def reply(self,name):
        return ("%s,到"%name)

class Class:

    def __init__(self,class_name,student = []):
        self.student = student
        self.class_name = class_name


    def add_student():
        name = input("请输入名字：")
        age1 = input("请输入年龄：")
        num1 = input("请输入学号：")
        name = Student(name, age1, num1)
        self.student.append(name)
    def del_student():
        name = input("请输入要删除学生的姓名")
        for stu in self.student[:]:
            if stu == name:
                del stu
    def say(self,name):
        return ("%s到了没',%name)
