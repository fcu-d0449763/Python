# 循环中的关键字

#break，continue，else,input

#练习：随机生成一个整数，然后去猜，猜中为止
'''
import random

number = random.randint(0,100)
count = 0
while True:
	num = input('请输入一个数字（1-100）：')
	count += 1 
	if int(num) == number:
		print('恭喜你，猜对了！ %d' % number)
		if count > 7:
			print('智商欠费，请充值')
		elif count > 3:
			print('机智')
		else:
			print('大神！！')

		break
	else:
		if int(num) > number:
			print('大了，再小点')
		else:
			print('小了，再大点')
'''

# 计算1000以内，不能被15整除的数的和

'''
sum1 = 0
for x  in range(1000):
	if x % 15 == 0:
		continue
	sum1 += x
	# print(x)
print(sum1)

'''
#Python中的循环的最后可以添加else语句，代表循环结束后要执行的代码
'''
for 变量 in 序列：
	循环体
else：
	循环结束后要执行的代码


while 条件语句：
	循环体
else:
	循环结束后要执行的代码

注意：写到else 里面的语句，和写在循环外边的区别是：
break的时候，else中的内容不会执行

'''
##print 的使用

'''
1.print（内容1）特点：一个print打印完内容后，默认会换行
2.一个print可以同时打印多个内容，多个内容之间用逗号隔开。打印效果
，多个内容之间用逗号隔开。
3.设置一个print打印结束后的样式（默认是换行）
end = 字符串
print('aaa',end = ',')
print ('bbb')


4.设置多个同时打印多个内容，内容之间的样式（默认是空格）

print('a','b','c',sep='')
'''