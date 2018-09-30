# @Author   :xaidc
# @Time     :2018/8/30 9:22
# @File     :02-匿名函数.py


'''
匿名函数本质还是函数，之前函数的所有内容都适用于它

1.函数的声明
函数名 = lambda 参数列表：返回值


2.说明：
函数名：变量名
lambda：声明匿名函数的关键字
参数列表：参数名1，参数名2.。
冒号：固定格式
返回值：表达式，表达式的值就是返回值

3.调用
匿名函数的调用和普通函数一样



'''
# 写一个匿名函数计算两个数的和
my_sum = lambda x,y:x+y
result = my_sum(10,20)
print(result)

# 练习，写一个匿名函数，获取指定的数字列表指定下标的值的1/2
# 匿名函数的参数可以设默认值
get_value = lambda list1, index=0: list1[index]/2
# 位置参数
print(get_value([1,2,3,4,5],3))
print(get_value([1,2,3,4,5]))
# 关键字参数
print(get_value(index=1,list1=[12,23,42,56]))



# 练习2：获取一个列表的所有的元素的和和平均值（sum函数可以计算第一个序列的和)

list_operation = lambda list1:(sum(list1),sum(list1)/len(list1))
sum1,average = list_operation([1,2,3,4,5,6])
print(sum1,average)



# python中的函数可以有多个返回值的。就是在一个return后返回多个值，多个值之间用逗号隔开