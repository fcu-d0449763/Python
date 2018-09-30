# @Author   :xaidc
# @Time     :2018/9/7 10:44
# @File     :05-属性的getter和setter.py

"""
保护类型的属性：
a.就是在声明对象属性的时候在属性名前加一个下划线来代表这个属性是受保护的属性。
那么以后访问这个属性的时候就不要直接访问，要通过getter来获取这个属性的值和setter来给这个属性赋值
b.如果一个属性已经声明成保护类型的属性，那我们需要给这个属性添加getter。也可以添加setter

2.添加getter
添加getter其实就是声明一个没有参数有一个返回值的函数
a.格式:
@property
def 去掉下划线的属性名(self):
    函数体
    将属性相关的值返回

b.使用场景
场景一：如果想要获取对象的某个属性的值之前，想要再干点儿别的事情（做额外的处理），就可以给这个属性添加getter
场景二：想要拿到某个属性被使用的时刻

3.添加setter
添加setter就是声明一个有一个参数但是没有返回值的函数。作用是给属性赋值
a.格式
b.使用场景

"""
class Car:
    def __init__(self):
        self.color = '黑色'
        self.type = '劳斯莱斯'
        # _price属性是保护类型
        self._price = '2亿'

    # 给_price属性添加getter
    @property
    def price(self):
        print('在使用_print属性')
        return self._price
    # 想要给一个属性添加setter，必须先给这个属性添加getter
    @price.setter
    def price(self,price):
        if isinstance(price,int) or isinstance(price,float):
            self._price = price
        else:
            self.price = 0

# 练习：声明一个员工类，其中有一个属性是是否已婚（bool），获取值之前根据存的值返回'已婚'/'未婚'
class Staff:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self._is_marry = True
    @property
    def is_marry(self):
        # return self._is_marry
        if self._is_marry:
            return '已婚'

        return '未婚'
    @is_marry.setter
    def is_marry(self,marry):
        self._is_marry = marry
    # @is_marry.setter
    # def is_marry(self,is_marry):
    #     if is_marry == True:
    #         self._is_marry = '已婚'
    #     else:
    #          self._is_marry = '未婚'
p1 = Staff('张三',1000)
print(p1.is_marry)
p1.is_marry = False
print(p1.is_marry)






if __name__ == '__main__':
    car1 = Car()
    # 添加完getter后就通过getter去获取属性的值
    # price 就是属性_price的getter
    print(car1.price)
    print(car1.color)

    car1.price = 1000
    print(car1.price)
    car1.price = 'abc'
    print(car1.price)