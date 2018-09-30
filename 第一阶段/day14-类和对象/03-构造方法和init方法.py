"""
1.构造方法：系统自动创建的，方法名和类名一样。用来创建对象
2. __init__"init方法的功能是用来初始化和添加赋属性的
当我们通过构造方法去创建对象的时候，系统会自动调用(不用自主调用init方法)
"""
class Dog:
    def __init__(self):
        print('init方法')


class Person():
    #init方法可以添加参数
    def __init__(self,name,age = 18):
        print(name,age)
        print('人类的init方法')
# 创建对象的过程：调用构造方法在内存中开辟一个对象，
# 然后用新建的这个对象去调用init方法，来初始化对象对象的属性。最后才将对象返回
dog1 = Dog()
#如果类的init方法有参数，通过给构造方法传参
p1 = Person('小明')
p2 = Person('小红',20)

