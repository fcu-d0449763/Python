# @Author   :xaidc
# @Time     :2018/8/29 16:40
# @File     :06-homework.py

# 1.编写一个函数，求1+2+3+...+N
'''
def sum1(N):
    count = 0
    for i in range(1,N+1):
        count += i
    return  count
print(sum1(10))
'''
#2.编写一个函数，求多个数的最大值
'''
def maxlist(list1):
    num1 = list1[0]
    for item in list1:
        if item > num1:
            num1 = item
            continue
    return num1
list2 = [1,21,3,34,5,35]
print(maxlist(list2))
'''
#3. 编写一个函数，实现摇骰子的功能，打印n个色子的点数和
'''
import random
def sum_point(n):
    count = 0
    for i in range(n):
        point = random.randint(1,6)
        print('骰子点数分别为：%d'%point,sep = ' ')
        count += point
    return count
print("点数和为%d"%sum_point(3))
'''
# 4.编写一个函数，交换指定字典的key和value。
# 例如：{'a':1,'b':2,'c':3} -->{1:'a',2:'b',3:'c'}
'''
dict1 = {'a':1,'b':2,'c':3}
dict3 = {}
def exchange_dict(dict2:dict):
    for key in dict2:
        dict3[dict2[key]] = key
    return dict3
print(exchange_dict(dict1))
'''
# 5.编写一个函数，求三个数的最大值
'''
def max_num(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b

print("这三个数最大值是：%d" % max_num(2,34,13))
'''
# 6.编写一个函数，提取指定字符串中的所有的字母，然后拼接在一起后打印出来
# 例如：'12a&bc12d--'--->'abcd'
'''
def string(str1:str):
    str2 = ''
    for i in range(len(str1)):
        if 'a' <= str1[i] <= 'z'  or 'A' <= str1[i] <='Z':
            str2 += str1[i]
    print(str2)
string('12a&bc12d--')
'''
# 7.写一个函数，求多个数的平均值
'''
def avg_num(*num):
    sum1 = 0
    for i in num:
        sum1 += i
    avg1 = sum1/len(num)
    return avg1
n = avg_num(1,4,5,7)
print("平均数是：%.2f"%n)
'''
# 8.写一个函数，默认求10的阶乘，也可以求其他数的阶乘
'''
def jiecheng(n = 10):
    count = 1
    for i in range(1,n +1):
        count *= i
    return count
num = jiecheng()
print("这个数的阶乘是：%d"%num)
'''
# 9.写一个函数，可以对多个数进行补贴的运算
# 例如：operation('+',1,2,3)-->求1+2+3的结果
#      operation('-',9,8)-->求9-8的结果
#      operation('*',2,4,8,10)-->求2*4*8*10的结果
def operation(str1:str,*num):
    if str1 == '+':
        count1 = 0
        for i in num:
            count1 += i
        return count1
    if str1 == '-':
        nums = num[0] - num[1]
        return nums
    if str1 == '*':
        count2 = 1
        for j in num:
            count2 *= j
        return count2
num1 = operation('+',1,2,3)
num2 = operation('-',9,8)
num3 = operation('*',2,4,8,10)
print(num1,num2,num3,sep='\n')

