#字符串的格式化
# '格式符'%（格式符对应的值）
# 说明：%是固定的格式吧;
# %s 字符串
# %d 整数
# %f 浮点数
# %c 字符    可以将数字转换成字符拼接到字符串中
# %x/x 十六进制

first_name ='jiang'
last_name= 'xiucheng'

age=21

print('%s%s%d' % (first_name,last_name,age))


num=100
print( '%.8f' % num)



# 练习：使用变量保存学生的名字，年龄和成绩

name = 'xaidc'
age = 13
grade = 100
print('%s今年%d岁，他的成绩是%.1f' % (name,age,grade))