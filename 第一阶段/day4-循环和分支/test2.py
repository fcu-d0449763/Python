# if 语句
# Python中的分支结构只有一种：if 分支结构

'''
1.if 
if 条件语句：
	执行语句块


说明：
a.i：Python中的关键字，’如果‘的意思，用来做判断
b.条件语句：最终的结果会被转换成布尔值
c.冒号：冒号是固定写法，必须写
d.执行语句块：这儿可以是多行语句，但是每行语句必须和前面的if保持一个缩进

执行过程:先判断条件语句的结果是否为true，如果为true就执行冒号后面的执行语句块。
         否则直接执行if模块后的其他语句


'''
age = 18
if age >= 18:
	print('成年')
elif age <18:
	print('不成年')


# 练习：用一个变量保存一个学生的成绩，要求：当学生的成绩大于90的时候，打印优秀
   # 不管成绩是多少，都把成绩打印出来
grade = 98
if grade > 90:
	print('优秀')
print("成绩：%d" % grade )


'''
2.if-else
语法：
if 条件语句：
	执行语句块1
else：
	执行语句块2
其他语句

说明：
else：关键字（else后面的冒号不能省）

执行过程：先判断条件语句的结果是否为true，如果是就执行语句块1
           执行完语句块1后再执行其他语句；如果为false就执行语句块2，
           执行完语句块2后再执行其他语句
'''
"""
3.if -elif-else


"""
# 要求成绩大于90分打印优秀，80-90打印良好，60-79及格，60以下不及格

grade=95
if grade>=90:
	print('优秀')
elif 80<=grade<90:
	print('良好')
elif 60<=grade<80:
	print('及格')
else:
	print('不及格')


'''

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")
'''


'''

4.if 语句的嵌套
每个if分支之中都可以嵌套其他的if语句
if 条件1：
	执行语句1
	if 条件2：
		执行语句2
	else:
		执行语句3
else：
	执行语句4
'''

#成绩和年龄：如果成绩大于等于90并且年龄是18以上就获取奖金100，
#             年龄小于18就获取奖金200.成绩小于90不管多少岁打印没有奖金


score = 90
age = 20
if score>= 90:
	if age >=18:
		print('100')
	else:
		print('200')
else:
	print('没有奖金')



# 练习：产生一个随机数，判断随机数是否是偶数，如果是打印偶数，否则打印奇数。
		# 如果能被4整除，再打印能被4整除

#import 是Pyt内容hon中导入模块或者模块中内容的关键字
#random是Python内置的产生随机数的模块
import random

num = random.randint(1,200)#产生一个一到200的随机数
print(num)
if num%2 ==0:
	print("偶数")
	if num%4 ==0:
		print("能被4整除")
else:
	print("奇数")