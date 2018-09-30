# @Author   :xaidc
# @Time     :2018/9/7 10:19
# @File     :04-属性的私有化.py
"""
python中并没有真正的私有化！

1.私有化
a.类中的属性和方法都可以通过在属性名和方法名前加两个下划线，来让属性和方法变成私有的
b.私有的属性和方法只能在当前的类中使用

2.私有化原理
在前面有两个下划线的属性名和方法名前添加了'_类名'来阻止通过直接访问属性名来使用属性
"""
class Dog:
    # 字段
    number = 100
    __count = 20

    def __init__(self):
        # 对象的属性
        self.color = 'yellow'
        self.age = 3
        self.name = '大黄'
        self.__sex = 'boy'
#     对象方法
    def eat(self):
        print('%s在吃屎~'% self.name)

#     类方法
    @classmethod
    def shout(cls):
        print('汪汪汪')
#     静态方法
    @staticmethod
    def function():
        print('看家！！')
#python的类中默认的属性和方法是公开的
dog1 = Dog()
print(Dog.number)
print(dog1.name,dog1.color,dog1.age)
dog1.eat()
Dog.shout()
Dog.function()

# 在类的外面不能直接使用私有的属性
# print(Dog.__count)
# print(dog1.__sex)
print(dog1.__dict__)

if __name__ == '__main__':
    pass