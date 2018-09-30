'''
编程实现（for和while各写一遍）
1.求1到100之间的所有数的和，平均值
2.计算1到100之间能3整除的数的和
3.计算1到100之间不能被7整除的和
'''
#1.for
num1 = 0
for i in range(0,101):
	num1 += i
avg1 = num1/i
print("1-100的所有数的和为%d，平均值为%.2f" % (num1,avg1))

#1.while
x=1
num2=0
while x <= 100:
	num2 += x
	x += 1
avg2=num2/(x-1)
print("1-100的所有数的和为%d，平均值为%.2f" % (num2,avg2))

#2.for
num3 = 0
for y in range(1,101):
	if not y % 3:
		num3 += y
print("1-100之间能3整除的数的和为：%d" % num3)

#2.while 
n = 1
num4 = 0
while n <= 100:
	if not n % 3:
		num4 += n
	n += 1
print("1-100之间能3整除的数的和为：%d" % num4)

#3.for
num5 = 0
for a in range (1,101):
 	if a%7:
 		num5 += a
print("1-100之间不能被7整除的数的和为：%d" % num5)

#3.while 
z = 1
num6 = 0
while z <= 100:
	if z%7 :
		num6 += z
	z += 1
print("1-100之间不能被7整除的数的和为：%d" % num6)
