# @Author   :xaidc
# @Time     :2018/9/3 14:40
# @File     :04-异常捕获.py
import json
"""
1.为什么要使用异常捕获
异常：程序崩溃了，报错了。。。

程序出现异常，但是不想因为这个异常而让程序崩溃。这个时候就可以使用异常捕获机制
2.怎么捕获异常
a.形式一：捕获try后代码里面的所有异常
try:
    需要捕获异常的代码块（可能会出现异常的代码块）
except:
    出现异常后执行代码
其他语句
    
执行过程：执行try后面的代码块，一旦遇到异常，就马上执行except后面的代码块。执行完后再执行其他的语句
        如果try里面的代码块没有出现异常，就不执行except后面的代码块，而是直接执行其他语句
b.形式二：
try：
    需要捕获异常的代码块（可能会出现异常的代码块）
except 错误类型：
    出现异常后执行代码
    
执行过程：执行try后面的代码块，一旦遇到异常，就马上执行except后面的代码块。执行完后再执行其他的语句
        如果try里面的代码块没有出现指定的异常，就不执行except后面的代码块，而是直接执行其他语句
c.形式3
try:
    需要捕获异常的代码块（可能会出现异常的代码块）
except (错误类型1，错误类型2...):
    出现异常后执行代码


d.形式4
try：
    需要捕获异常的代码块（可能会出现异常的代码块）
except 错误类型1：
    执行语句块1
except 错误类型2：
    执行语句块2
    
    
d.形式5
try：
    需要捕获异常的代码块（可能会出现异常的代码块）
except：
    出现异常的执行代码
finally：
    不管有没有捕获到异常（就算崩溃了也会执行）
    （在这儿做程序异常退出时的善后，一般做保存数据的进度的工作）
    
3.抛出异常（后面补充）
raise 错误类型

"""


# 1.什么情况。。。
# a.输入俩个数，然后求这个两个数的商是多少
# num1 = float(input("除数："))
# num2 = float(input("被除数："))
# print("%f / %f = %f"% (num1,num2,num1/num2))


# b.打开一个不存在的文件，不希望程序崩溃，只是让读出的内容是空

try:
    with open('./files/info.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
except FileNotFoundError:
    print("没有找到该文件")
# 2.捕获异常
b = [1,2,3,4,5]
try:

    print(b[6])
except:
    print('下标越界')
print('=========')

dict1 = {'a':12,'b':23}
try:
    print(dict1['c'])
    print(b[6])

except IndexError:
    print('下标越界')
except KeyError:
    print('key错误')


