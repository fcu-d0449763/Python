# @Author   :xaidc
# @Time     :2018/9/14 8:52
# @File     :01-内存管理机制.py
'''
掌握:1.数字(0-255),字符串(简单的字符串),布尔值的缓存
    2.垃圾回收机制中的引用计数机制

1.python中变量的赋值
python中所有的数据都是对象,所有的变量都是对象的引用
python 对数字,字符串和布尔对象进行缓存,让不同的变量赋同样值的这些对象,给的地址是缓存的对象的地址
总结:1.给一个变量赋值的时候,赋的是数字,字符串,布尔的时候,会现在缓存区中是否有这个值
如果有直接将值对应的地址赋给变量.没有就在缓存中开辟空间存储数据,然后返回地址.
2.给一个变量赋值的时候,赋的是除了数字,字符串,布尔以外的值,就直接在内存中开辟空间存储数据,然后返回地址
一个变量存了一个对象的地址,那么这个变量就是这个对象的引用


2.python中的内存管理
C的内存管理机制:手动
java\oc\python等:拥有一套属于自己的自动内存管理机制

a.python通过垃圾回收机制来对内存进行管理的:不定时对程序中的对象进行检测,看是否需要回收(将对象的内存释放)
看是否需要回收就看对象的引用计数是否为0,为0就回收
b.引用计数
python中每个对象在创建的时候就会有一个属性叫引用计数,其对应的值是0
当对象被引用依次,其引用计数就会加1.当对象的引用减少一个,其引用计数就会减1

3.垃圾回收机制
垃圾回收机制并不是一旦产生引用计数为0的对象就马上回收.而是不定时的对整个程序中所有的对象进行检测,检测的时候引用计数为0才回收
当当前程序所有的对象引用计数变化的次数达到他的阀值,才会对对象进行检测

4.循环引用(python的垃圾回收机制,能够自动解决因为循环引用而导致的内存泄漏问题)
检测的时候如果对象(object_i)的引用计数不是0,就备份引用计数值,去找到引用这个当前对象的对象(object_j),
然后将object_j的引用计数count_j减1,如果count_j减1后的值是0,那么count_i的值就减1.
如果剪完后count_i的值也是0,那么object_i就会销毁
'''
from sys import getrefcount
if __name__ == '__main__':
    object1 = [2,2]
    object2 = object1
    # 注意:gerrecount函数本身会对查看的对象进行引用
    print(getrefcount(object1))

    num = 100
    print(getrefcount(num))