# @Author   :xaidc
# @Time     :2018/8/27 15:51
# @File     :07-认识元组.py

# tuple(元组)
# 元组就是不可变的列表。列表中除了和可变的相关内容以外，其他的全部都适用于元组
#不支持增，删除，修改，只支持和查的相关操作
# 1.声明元组
tuple1 = (1,2,3,10)
print(tuple1,type(tuple1))
# 注意：如果要写一个元组元素个数是1的字面量，需要在那一个元素的后面加逗号
t2 = (100, )
print(t2,type(t2))

t3 = ()
print(t3,type(t3))

# 特殊操作
point = (100,200,'red')
print(point[0],point[1])
#通过两个变量来获取元组中的唯一的两个元素的值
x, y , color= point
print(x,y)
#通过在变量前加*，获取元组/列表中的一部分，结果是一个列表
user = ('小吕', 90, 98, 56,100, '男')
name, *score, sex = user
print(name,score,sex)

#4.多个值之间用逗号隔开，对应的数据也是元组
a1 = 1,2,3,4  #相当于a = （1,2,3,4）
print(a1,type(a1))


x,y = 100,200 #相当于x,y = (100,200)
print(x,y)