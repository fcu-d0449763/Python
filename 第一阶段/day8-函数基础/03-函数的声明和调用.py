# @Author   :xaidc
# @Time     :2018/8/29 9:26
# @File     :03-函数的声明和调用.py

'''
1.什么是函数：函数就是对实现某一特定功能的代码的封装
2.函数的分类：内置函数和自定义函数
内置函数：系统写好的，可以直接使用的函数。例如：print函数，input函数，sum函数，len函数等等
自定义函数：程序员自己去创建的函数

3.函数的定义（函数的声明）：
a.固定格式
def 函数名(参数列表)：
    函数体

4.说明：
def：Python中声明函数的关键字
函数名：标识符，不能是关键字；PEP8，见名知义(看到函数名要大概知道函数的功能)
（）：固定格式，并且必须写。
参数列表：参数名1，参数名2，参数名3...；参数可以有多个，也可以没有。这儿的参数也叫形参
        参数是用来从函数的外面，向函数里面传值用的（将数据从函数的外面传递到函数的里面）

函数体：实现函数功能的代码段，函数体中可能会包含return语句


5.初学者声明函数的过程：
第一步：确定函数的功能
第二步：确定函数名
第三步：确定参数（确定有没有，有几个）
        看实现函数的功能，需不需要从函数的外面传递数据进来，需要几个就定义几个参数
第四步：实现函数功能
第五步：确定返回值

6.注意：
（特别重要！）函数体只有在调用的时候才会执行
7.函数调用
a.固定格式
函数名（实参列表）
b.说明：
函数名：你要调用哪个函数，就写对应的函数名。函数只能先声明才能调用
实参列表：就是用来给形参传值的
'''

# 写一个函数打印两个数的和
def my_sum(num1,num2):
    print(num1 + num2)
my_sum(1,2)
# 一个函数可以调用多次
'''
8.函数的调用过程（强调！！！必须掌握）
a.回到函数声明的位置
b.使用实参给形参赋值（传参）---传参的时候一定要保证每个形参都有值
c.执行函数体
d.将返回值返回给函数调用者
e.回到函数调用的地方，接着往后执行
'''
# 练习：写一个函数，打印一个整数的阶乘
def jiecheng(num):
    count = 1
    for i in range(1,num +1):
        count *= i
    print(count)
jiecheng(4)