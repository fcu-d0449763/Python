# @Author   :xaidc
# @Time     :2018/9/7 14:40
# @File     :07-方法的重写.py
"""
子类继承父亲，拥有父亲的属性和方法以后，还可以再添加自己的属性和方法
1.添加方法
直接在子类中声明相应的方法

2.添加对象属性
对象的属性是通过继承父类的init方法而继承下来
如果想要在保留父类的对象的同时添加自己的对象属性，需要在子类的init方法中通过super()去调用父类的方法

3.方法的重写
在子类中重新实现父类的方法，就是重写
方法一：直接覆盖父类的实现
方法二：保留父类的功能再添加其他功能

4.类中方法的调用过程（重点）
现在当前这个类中去找，没有就去父类中找，找不到就再去父类的父类中找，依次类推。
如在基类中都没有找到才崩溃。在第一次找到的位置，去调用

注意：使用super的时候必须是通过super（）来代替父类或者是父类对象
"""
class Animal:
    def __init__(self):
        self.age = 0
        self.sex = '雌'
    def shout(self):
        print('嗷嗷')
class Cat(Animal):
    def __init__(self):
        #调用父类的init方法
        super().__init__()
        self.name = '小花'


    food = '鱼'

    def shout(self):
        print('喵喵~')

class Dog(Animal):
    def shout(self):
        # 通过super（）调用父类的方法，保留父类的功能
        super().shout()
        print('汪汪~')
cat1 = Cat()
print(cat1.age)
print(cat1.name)
cat1.shout()

dog1 = Dog()
dog1.shout()
