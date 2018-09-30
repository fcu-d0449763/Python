# 1.查：获取列表元素
"""
a.获取单个元素：列表[下标]
下标范围：0~元素个数-1或者-1~-元素个数
注意：下标不能越界
"""
TV_names = ['请回答1988','琅琊榜','天龙八部','尼基塔']
print(TV_names[1],TV_names[-1])


# b.获取部分元素(切片):(和字符串一样)
# 注意步进
# 切片的结果是列表
print(TV_names[1:3])
print(TV_names[-1:-3:-1])

# c.遍历（一个一个的获取每个元素）
# 可以将列表之间放到for 循环的in 后边
# 循环过程中，for 后面的变量取得是列表中的每个元素
for item in TV_names:
    print(item)


# 练习： 写一个列表统计>80的个数
count = 0
grade = [23,68,89,98,67,45]
for i in range(6):
    if grade[i] > 80:
        count +=1
print (count)

# 2.改(修元素的值)
# 语法：列表名[下标] = 新值通过下标获取元素，然后重新赋值）
person = ['小马',23,'篮球']

# 修改person 列表中下标是1的元素的值
person[1] = 25
print(person)

#3 增(增加列表的元素，添加元素)
# 注意： 列表中元素的个数发送改变后，列表中的元素的下标会根据新的位置重新分配
# a.列表.append(元素）：在列表的最后去添加一个元素
person.append('男')
print(person)

# b.列表.insert（下标，元素）：在指定的下标前插入一个元素
person.insert(0,'001')
print(person)

person.insert(2,'H5')
print(person)

# 录入五个学生的成绩，并且保存在一个列表中

'''
num = []
while True:
    grade = int(input("请输入学生的成绩（以0结束）："))
    if grade == 0:
        break
    num.append(grade)
print(num)
'''
# 删（删除列表中的元素）
# a.del 列表[下标] --> 根据下标取删除列表中的元素
# del 语句是Python 中删除数据的语法，它可以删除任何数据：del 变量（删除变量） del 列表（删除整个列表）
foods = ['辣条','棒棒糖','大蒜','火锅','饼干','小龙虾','大龙虾','花甲']
del foods[2]
print(foods)

del foods[4]
print(foods)

# b.列表.remove (元素) -->删除列表中的某个值
# 注意：如果这个元素在列表中有多个，只删除最前面的那一个
foods.remove('饼干')
print(foods)

# c.列表.pop(下标)---> 将列表中指定下标对应的元素取出来
food = foods.pop(1)  #将foods中下标是1 对应的元素取出来，保存到变量food中
print(foods,food)

# 想进一切办法，将一个保存成绩的列表中，成绩低于60分的全部删除
# [78,59,40,90,89,45,69,30] -->[78,90,89,69]
numbers = [78,59,40,90,89,45,69,30]
num = []
for number in numbers:
    num = numbers
    for i in range(len(num)):
        if num[i] < 60:
            del num[i]
            break
print(numbers)


scores = [78,59,40,90,89,45,69,30]
for score in scores[:]:
    if score < 60:
        scores.remove(score)
print(scores)

#注意：以后遍历列表的元素的时候，我们一般遍历它的拷贝的值（[:]）