# @Author   :xaidc
# @Time     :2018/8/29 13:55
# @File     :05-函数的返回值.py

'''
1.返回值：函数的返回值就是return关键字后面的表达式的值，就是函数调用表达式的结果
2.Python中所有的函数都有返回值，默认是None(没有return)

说明：
a.如果函数体没有return，函数的返回值就是None
b.调用函数的语句就是函数调用表达式
'''

# 写一个函数，打印hello
def hello():
    print('hello')

re = hello()
print(re)

# 2.return 关键字（只能写在函数体中）
'''
a.确定返回值
b.结束函数（函数中只要遇到return，函数就直接结束）
c.单独的return相当于return None
'''
def func1(n):
    print(n)
    return 100
    print('===')
re = func1(10)
print(re)
'''
注意：看一个函数的返回值是多少，不是看函数中有没有return，而是看函数的执行过程中遇没有遇到return
    遇到了，就是return后面的结果，否则就是None
'''

# 练习：写一个函数，判断一个数是否是偶数，如果是返回True，否则返回False
def num(n):
    if n %2 ==0:
        return  True
    else:
        return False
print(num(4))

'''
什么时候函数需要返回值
只要实现函数功能会产生新的数据，就通过返回值将新的数据返回，而不是打印它
'''
# 1.练习：写一个函数，统计一个列表中浮点数的个数
def isint(list1):
    count = 0
    for i in list1:
        if isinstance(i,float):
            count += 1
    return count
num = isint([1,2.2,2.0,22,33])
print(num)

# 2.写一个函数，将一个数字列表中所有的元素的值都变成原来的二倍
def double(list2):
    list4 = []
    for i in list2:
        i = 2*i
        list4.append(i)
    return list4
print(double([1,2,3]))

# 3.写一个函数，获取指定元素对应的下标
def indexs(list1:list,item):
    index_list = []
    for index in range(len(list1)):
        if list1[index] == item:
            index_list.append(index)
    return index_list
print(indexs([1,2,3,42,3,3,21,2],2))

# def index1(n):
#     list3 = [1,2,3,4]
#     num = 0
#     for i in list3:
#         if i == n:
#             break
#         num += 1
#     return num
# print(index1(4))



# 补充：判断一个值是否是指定的类型
# isinstance(值，类型)----返回值是布尔
# print(isinstance(10,int))判断10是否是int类型