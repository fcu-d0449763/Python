# @Author   :xaidc
# @Time     :2018/8/28 9:07
# @File     :02-字典.py

# 字典(dict)
'''
1.字典是容器类型（序列），以键值对作为元素（字典里面存的数据全是以键值对的形式出现的）
{key1:value1,key2:value2...}
2.键值对： 键：值 （key：value）
键（key）：要唯一，不可变的(数字，布尔，字符串，元组，推荐使用字符串)
值(value):可以不唯一，可以是任何数据类型的数据
3.字典是可变的（增删改）---可指的是字典中的键值对的值和个数可变
'''
# 1.声明字典
dict1 = {'name':'tony', 'sex':'男', 'age':100,'job':'doctor'}
print(dict1,type(dict1))

# dict2 = {}  # 空的字典

# 2.查（获取值）
# 获取字典的元素对应的值（字典存数据，实质还是存的value，key 是获取value的手段）
#a. 字典[key]
print(dict1['name'])

# 通过字典[key]获取value的时候，如果不存在会发生keyerror 异常
# b.字典.get(key）
# 字典.get(key）,如果key不存在不会报错，返回None
print(dict1.get('abc'))  #None---Python中的特殊值，代表没有

# 总结：确定key值肯定存在用[]语法获取value。
# key值可能不存在，不存在的时候不希望报错，而是想要自己对他进行特殊处理的时候使用get获取value
person = {'name':'coco','age':19,'grade':99}
# 想要获取性别sex，如果没有就默认为’男‘
if person.get('sex') != None:
    print(person['sex'])
else:
    print('男')


# c.遍历字典
# 遍历字典直接取到的是字典所有的key值
for key in person:
    # 打印key
    print(key)
    print(person[key])


# 3.改（修改key对应的value）
# 字典[key] = 新值   （key 本来就存在）
person['name'] = 'tony'
print(person)

# 4.增（添加键值对）
# 字典[key] = 值  （key 本来不存在）
person['sex'] = '男'
print(person)

# 5.删（删除键值对）
# a. del 字典[key]
del person['sex']
print(person)

# b.字典.pop(key)
name = person.pop('name')
print(name,person)