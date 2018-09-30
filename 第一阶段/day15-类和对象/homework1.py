# @Author   :xaidc
# @Time     :2018/9/7 18:39
# @File     :homework1.py
"""
定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
方法： a. 获取学生的姓名：getname() b. 获取学生的年龄：getage()
        c. 返回3门科目中最高的分数。get_course()
"""
class Student:
    def __init__(self,name,age,*score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def get_course(self,*score):
        list1 = list(self.score)
        x = max(list1)
        return x
stu1 = Student('小明',18,78,89,78)
print(stu1.get_name())
print(stu1.get_age())
print(stu1.get_course())
