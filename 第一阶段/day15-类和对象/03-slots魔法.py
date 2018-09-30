# @Author   :xaidc
# @Time     :2018/9/7 9:52
# @File     :03-slots魔法.py
class Person:
    # 通过__slots__中存的元素的属性的值来约束当前这个类的对象的属性。对象的属性只能比元组中的元素少，不能多！
    __slots__ = ('name','age','face')

    def __init__(self):
        self.name = '张三'
        self.age = 18
        self.face = 70
        # self.sex = 'male'  #__slots__中并没有sex

if __name__ == '__main__':
    p1 =  Person()
    # p1.sex = 'male'
    # print(p1.sex)
    p1.name = '小明'

    #注意：一旦在类中给__slots__属性赋了值，那么这个类的对象的__dict__属性就不能使用了
    # print(p1.__dict__)