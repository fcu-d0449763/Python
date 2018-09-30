# @Author   :xaidc
# @Time     :2018/8/28 14:19
# @File     :05-集合.py

# 集合（set）
# 集合是Python 中一种容器类型;无序的，可变的,值唯一
# 和数学中的集合差不多
# 1.声明一个集合
set1 = {1,'abc',100,100}
print(set1,type(set1))

set2 = set('abshdjssa')#自带一个去重的功能
print(set2)
# 可变的都不能成为集合中的内容，其他的基本都行，数字，布尔和字符串是可以的

# 2.查(获取集合中元素)
# 集合是不能单独获取其中的某一个元素的
# 遍历获取每一个元素

# 3.增（添加元素）
# a.集合.add(元素)
set1.add('good')
print(set1)

# b.集合1.update(集合2):将集合2中的元素，添加到集合1中

# 4.删
# 集合.remove(元素)
set1.remove('abc')
print(set1)

# 删除所有的元素

set1.clear()
print(set1)

# 5.改不了

# 6.数学相关的集合或运算
# a.判断包含情况：集合1 >= 集合2 ：判断集合1中是否包含集合2
# 集合1 <= 集合2：判断集合2是否包含集合1
print({1,2,3,4,5} >= {2,3,1})

# b.求并集 ：|
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,14,15,16}
print(set1|set2)

# c.求交集：&
print(set1&set2)


# d.求查集：-
print(set1-set2)
print(set2-set1)

# e.求补集
# 求两个集合中除了公共部分以外的部分
print(set1^set2)