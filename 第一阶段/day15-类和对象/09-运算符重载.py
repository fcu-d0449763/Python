# @Author   :xaidc
# @Time     :2018/9/7 15:56
# @File     :09-运算符重载.py

"""
如果希望类的对象支持相应的运算符操作（例如：+，-，*，/,>,<等），就必须实现相应的魔法方法
这个过程就叫运算符的重载

+:__add__(self, other)
>:__gt__(self, other)
一般情况下需要对 > 或者<进行重载，重载后可以通过sort方法直接对对象的列表进行排序
"""
class Student:
    def __init__(self,name = '',age = 0,score = 0):
        self.name =  name
        self.age = age
        self.score = score
    # self:+号前面的对象
    # other：+号后面的对象
    def __add__(self, other):
        return self.score + other.score
    # 注意：重载>和<可以值重载换一个，另外一个对应的功能自动取反
    def __gt__(self, other):
        return self.age > other.age

    # 重写魔法方法__str__,用来定制对象的打印样式
    def __str__(self):
        # return '%s,%d,%d'%(self.name,self.age,self.score)
        return str(self.__dict__)[1:-1]
class SchoolChild(Student):
    pass

stu1 = Student('小明',32,34)
stu2 = Student('小红',23,90)
stu3 = Student('小强',34,89)
print(stu1)
all_students = [stu1,stu2,stu3]
all_students.sort()
for stu in all_students:
    print(stu.name,stu.age,stu.score)




print(stu1 + stu2)
print(stu1 > stu2)
print(stu1 < stu2)

# 运算符重载支持继承
c1 = SchoolChild('COCO',12,34)
c2 = SchoolChild('cc',23,67)
print(c1 + c2)