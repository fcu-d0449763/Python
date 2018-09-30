# @Author   :xaidc
# @Time     :2018/9/6 11:24
# @File     :05-对象属性的增删改查.py
"""
python 是动态语言，python中类的对象的属性可以进行增删的操作
"""
class Person:

    def __init__(self):
        self.name = 'jxc'
        self.age = 28
        self.height = 170



if __name__ == '__main__':
    #1.查（获取属性的值）
    p1 = Person()
    """
    方法一：对象.属性名
    方法二：def getattr(对象, 属性名, 默认值)
    方法三：对象.__getattribute__(属性名)
    """
    print(p1.name)
    # print(p1.name2)  #属性不存在会报错
    print(getattr(p1,'name'))
    print(getattr(p1,'name2',0)) #属性不存在可以通过设置默认值，让程序不崩溃，并且返回默认值
    print(p1.__getattribute__('height'))

    # 2.改（修改属性的值）
    """
    方法一：对象.属性 = 新的值
    方法二：def setattr(对象，属性名，新值)
    方法三：对象.__setattr__(属性名，新值)
    """
    p1.name = '李四'


    setattr(p1,'age',20)
    print(p1.age)

    p1.__setattr__('height',160)
    print(p1.height)
    #3.增（添加属性--属性不存在）
    # 注意：添加属性只能给某一个对象添加对应的属性
    """
    方法一：对象.属性 = 新的值
    方法二：def setattr(对象，属性名，新值)
    方法三：对象.__setattr__(属性名，新值)
    """
    p1.sex = '女'
    print(p1.sex)

    setattr(p1,'weight',40)
    print(p1.weight)

    p1.__setattr__('color','green')
    print(p1.color)

    # 4.删（删除对象属性）
    # 注意：删除值针对指定的对象
    """
    方法一：del 对象.属性
    方法二：def delattr(对象, 属性名)
    方法三：对象.__delattr__(属性名)
    """
    del p1.name

    delattr(p1,'age')

    p1.__delattr__('height')







