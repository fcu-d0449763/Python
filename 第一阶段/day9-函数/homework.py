# @Author   :xaidc
# @Time     :2018/8/30 18:20
# @File     :homework.py
# 1.写一个函数将指定列表中的元素逆序（例如[1,2,3] ->[3,2,1])(注意不要使用列表自带的逆序函数）
'''
def my_reverse(list1:list):
    list2 = []
    i = 1
    for _ in range(len(list1)):
        list2.append(list1[-i])
        i += 1
    return list2
list3 = [1,2,3,4,5]
print("列表：",list3)
print("逆序输出为:",my_reverse(list3))
'''
# 2.写一个函数，提取出字符串中所有奇数位上的字符
'''
def cut_string(str1:str):
    str2 = ''
    i = 1
    while i <= len(str1):
        str2 += str1[i]
        i += 2
    return str2
str3 = '0123456789'
print("字符串位：",str3)
print("该字符串奇数位上的字符位：",cut_string(str3))
'''
# 3.写一个匿名函数，判断指定的年是否是闰年
'''
Is_leapyear = lambda year : bool(( year%4 ==0 and year%100 != 0) or year%400 ==0)
year1 = 2008
BOOL = Is_leapyear(year1)
if BOOL:
    print("%d 是闰年"%year1)
else:
    print("%d 不是闰年"%year1)
'''
# 4.使用递归打印：
'''
n =3
@
@@
@@@
'''
# def at(n):
#     if n == 0:
#         return None
#     at(n-1)
#     print('@'*n)
# at(4)



# 5.写函数，检查传入列表的长度，如果大于2，那么保留前两个长度的内容，并将新内容返回给调用者
'''
def cut_list(list1:list):
    list2 = []
    if len(list1)>2:
        list2.append(list1[0])
        list2.append(list1[1])
    return list2
list3 = [1,2,3,4,5,6,7]
print("列表：",list3)
print("保留前两个长度后：",cut_list(list3))
'''
# 6.写函数，利用递归获取斐波那契数列中第10个数，并将该值返回给调用者。
'''
def feibo(n):

    if n == 1 or n ==2:
        return 1
    return feibo(n-1)+feibo(n-2)
print("第十个数是",feibo(10))
'''
# 7.写一个函数，获取列表中的平均值和最高分
# def avg_max(list1:list):
#     list1.sort()
#     max = list1[-1]
#     count = 0
#     for item in list1:
#         count += item
#     avg = count/len(list1)
#     return max,avg
# list3 = [78,23,56,87,66]
# max1,avg1 = avg_max(list3)
# print("列表为：",list3)
# print("最高分为：%d,平均分：%d"%(max1,avg1))

# 8.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新的列表返回给调用者
'''
def cut(n):
    list1 = []
    i = 1
    while i <= len(n):
        list1.append(n[i])
        i += 2
    return list1
list2 = [0,1,2,3,4,5,6,7,8,9]
tuple = (0,1,2,3,4,5,6,7,8,9)
list3 = cut(list2)
list4 = cut(tuple)
print(list3,list4,sep = '\n')
'''
# 9.写一个属于自己的数学模块（封装自己认为以后常用的数学相关的函数和变量）
# 和列表模块（封装自己以为以后常用的列表的相关操作）