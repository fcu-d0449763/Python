"""
list
1.列表是Python中的容器类型。有序的，可变的容器(可变指的是列表中的元素和元素的位置。个数可变)。
有序->可以通过下标来获取元素
可变->可以进行增删改（查）

2.元素：指的是列表中的每一个内容

"""
# 1.列表的声明
# a.声明变量赋一个列表值
scores = [29,23,45,32,345,543]
print(scores,type(scores),sep='\n')

person = ['tony',5,'boy']  # 一个列表中的元素的类型可以不一样
print(person)

# []代表空列表
names = []
print(names,type(names))

# b.将其他的数据类型转换成列表（只有序列才能转换：字符串和range，字典，元组，集合，生成式和迭代器）
chars = list('abcdef')
print(chars)

numbers = list(range(10))
print(numbers)

