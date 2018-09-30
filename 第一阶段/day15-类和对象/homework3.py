# @Author   :xaidc
# @Time     :2018/9/7 19:31
# @File     :homework3.py
'''
2.创建一个名为User 的类，其中包含属性firstname 和lastname ，
还有用户简介通常会存储的其他几个属性。在类User 中定义一个名 为describeuser() 的方法，
它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候
管理员是一种特殊的用户。
编写一个名为Admin 的类，让它继承User类。添加一个名为privileges 的属性
，用于存储一个由字符串(如"can add post"、"can delete post"、"can ban user"等)组成的列表。
编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。
'''
class User:
    def __init__(self,first_name,last_name,age,sex = '男'):
        self.first_name= first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describeuser(self):
        return '姓氏：%s,名：%s,年龄：%d,性别：%s'%(self.first_name,self.last_name,self.age,self.sex)
    def greetuser(self):
        return '%s%s,你好，祝你天天开心'%(self.first_name,self.last_name)
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        return '%s'%self.privileges

u1 = User('江','秀成',21)
print(u1.describeuser())
print(u1.greetuser())

A1 = Admin('江','秀成',21)
print(A1.show_privileges())