# @Author   :xaidc
# @Time     :2018/8/31 11:30
# @File     :03-生成器和生成式.py

'''
可以把迭代器看成一种容器，类似列表。生成器就是来生成迭代器。
'''

# 1.生成式(产生一个迭代器的表达式)
# 通过将生成式产生的迭代器转换成一个列表
# a 是生成器，能够生成0-9 中的所有的数字
a0 = (x for x in range(10))
a1 = (x*2 for x in range(10))
a2 = (char for char in 'h0e7l6l8o py2th4on' if '0'<=char<='9')
print('======')


#2.生成器和迭代器都是通过next来获取里面的数据
print(next(a0))
print(next(a0))
print(next(a0))
print('======')
for x in a0:
    print(x)
# 3.将生成器转换成列表
list1 = [x for x in range(10)]
print(list1)

#4.将生成器转换成字典
# 注意：容器类型的元素是元组，并且元素中有且只有两个元素的，才能转换成字典
dict = dict((x,x*2) for x in range(10))
print(dict)

# 一句代码实现交换一个字典中的key和value的值{'a':1,'b':2}-->{1:'a',2:'b'}
# dict2 = dict((value,key) for key,value in {'a':1,'b':2}.items())
# print(dict2)

old = {'a':1,'b':2}
dict3 = dict((old[key],key)for key in old)
print(dict3)