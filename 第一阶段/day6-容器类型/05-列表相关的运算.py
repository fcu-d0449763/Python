# @Author   :xaidc
# @Time     :2018/8/27 14:27
# @File     :05-列表相关的运算.py

#1. +操作
# 列表1+列表2：将列表1中元素和列表2中的元素依次合并，产生一个新的列表
a = [1,2]
list1 = [1,2]+['abc',100]
print(list1)

#2.*操作
# 列表1 * N：将列表1中元素重复N次，产生一个新的列表
list2 =a * 3
print(list2)

#3. in / not in
#元素 in 列表：判断一个元素是否在列表中
print(10 in [1,2,3,4])

#4. 求列表的长度
# len(序列)
print(len([1,2,3]))

#5. 相关的方法
#5.1 列表.count（元素）：统计指定的元素在指定列表中有几个
numbers = [1,2,1,3,45,1]
print(numbers.count(1))

#5.2 列表.extend（序列）：将序列中的元素添加到列表中
numbers.extend([100,200])
print(numbers)
#extend 和 append 的区别
numbers.append([100,200])
print(numbers)

# 5.3 列表.index（元素）：获取指定元素对应的第一个下标
print(numbers.index(1))

# 5.4 列表.pop():将列表中的最后一个元素从列表中取出来
item = numbers.pop()
print(numbers)

# 5.5列表.reverse()  将列表反序
numbers = [1,54,3,233,5]
numbers.reverse()
print(numbers)

# 5.6 列表.sort（） :对列表元素进行排序（默认是升序）
#列表.sort(reverse = True):对列表元素进行降序排序
numbers.sort()
print(numbers)

# 5.7 列表.clear():将列表中的元素全部清除
numbers.clear()
print(numbers)

#5.8 列表.copy():将列表中的元素全部拷贝一份产生一个新的列表，相当于列表[:]。
# 注意：这儿的拷贝是浅拷贝

numbers = [1,2,3,4]
numbers2 = numbers.copy()
print(numbers2)

