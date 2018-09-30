# @Author   :xaidc
# @Time     :2018/9/10 13:49
# @File     :03-day14作业评讲.py

# 1.电脑类
'''
class Computer:
    """电脑类"""
    def __init__(self,brand = '联想',color = '黑色',memory=0):
        self.brand = brand
        self.color = color
        self.memory = memory
    @staticmethod
    def play_game(game):
        print('玩儿%s' % game)
    @staticmethod
    def code(self):
        print('写python代码')
    @staticmethod
    def watch_video(video):
        print('在看%s'%video)

com1 = Computer(memory=512)
# 查
print(com1.color)
print(getattr(com1,'color','白色'))
# 改
com1.brand = '苹果'
setattr(com1,'brand','戴尔')
# 增
com1.size = 13.5
setattr(com1,'size',15)
# 删
del com1.size
delattr(com1,'memory')
'''
# 2.人和狗
'''
class Dog:
    """狗"""
    def __init__(self,name='',color='',age=0):
        self.name = name
        self.color = color
        self.age = age

    def shout(self):
        print('%s在汪汪叫!'%self.name)

class Person:
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age
        self.dog = None

    def took_dog(self):
#         能遛狗的前提是自己有狗
        if not self.dog:
            print('没有狗,自己遛自己吧!')
            return
        print('%s牵着%s在玩'%(self.name,self.dog.name))
p1 = Person('小明')
p1.dog = Dog('大黄','黄色',2)
p1.took_dog()
'''
# 3.学生和班级
class Student:
    '''学生'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = ''

    def response(self):
        '''答到'''
        print('%s,到!'%self.name)
    def show_info(self):
        print('姓名:%s 年龄:%d 学号:%s'%(self.name,self.age,self.id))

class Class:
    '''班级'''
    def __init__(self,name):
        self.students = []
        self.name = name
        self.__count = 0

    def add_student(self):
        '''添加学生'''
        name = input('姓名:')
        age = input('年龄:')

        # 学号
        self.__count +=1
        id = str(self.__count).rjust(3,'0')

        #创建学生对象
        stu = Student(name,int(age),id)

        #将学生保存到班级中
        self.students.append(stu)

    def del_student(self):
        '''删除学生'''
        del_name = input('请输入要删除的学生姓名:')

        for stu in self.students[:]:
            if stu.name == del_name:
                self.students.remove(stu)
                print('删除成功!')
                is_del = True
        if not is_del:
            print('没有该学生!')
    def call_names(self):
        '''点名'''
        for stu in self.students:
            print(stu.name)
            stu.response()

class1 = Class('python1806')
# 添加学生



# 数学
class Math:
    pi = 3.1415926
    e = 2.7

    @staticmethod
    def sum_double(num1,num2):
        return num1 + num2
    @classmethod
    def circle_area(cls,r):
        return cls.pi*r**2