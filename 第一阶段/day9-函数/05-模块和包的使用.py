# @Author   :xaidc
# @Time     :2018/8/30 15:23
# @File     :05-模块和包的使用.py
'''
封装：
1.函数：对实现某一特定功能的代码段的封装
2.模块：对变量。函数。类进行封装
模块：一个py文件就是一个模块

'''
def multiply(*numbers):
    sum1 = 1
    for item in numbers:
        sum1 *= item
    return sum1
print(multiply(1,2,5))

'''
1.怎么使用其他模块的内容？
a  import 模块
通过模块.内容的形式去使用模块中的内容（能够使用的是全局变量，函数，类）
b  from  模块 import  模块中的内容
可以直接使用模块中的内容

c  from 模块 import * --->将模块中的所有的内容都导入


2.重命名
import 模块 as 新名字
from 模块 import 内容 as 新名字

'''
'''

import my_list  #导入自定义模块
# 使用模块的全局变量
print(my_list.empty)
# 使用模块中的函数
num = my_list.count([1,2,3,4,5,6],1)
print(num)
import math #导入系统模块
print(math.pi)

'''

from my_list import count,empty
print(count([23,34,56,1,56],56))
print(empty)

from math import *
print(pi)
print(sqrt(4))

'''
# 将不希望被别的模块导入（执行）的代码放到模块的这个if语句中
if __name__ =='__main__':
    print('!',a)
    for x in range(10):
        print('!!',x)
        
每个模块都有一个__name__属性.这个属性的值默认就是当前模块的文件名
当当前模块正在被执行(直接在当前这个模块中点了run)的时候，__name__属性的值是'__main__'


在一个模块中，将不希望将其他模块导入的代码写在if __name = '__main__'中，
希望被导入的放在这个if外面

建议：函数的声明，类的声明一般写在if的外面，其他的写在if里面。（想要被外部使用的全局变量也可以写在外面）
'''

