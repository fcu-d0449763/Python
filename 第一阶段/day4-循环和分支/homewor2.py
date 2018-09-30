#1.求斐波那契数列中的第n个数的值：1，1,2,3,5,8,13,21,34...
n = int(input("输入你想求斐波那契数列第几个数的值："))
num1=num2=1
num=0
i = 2
while i < n :
	num=num1+num2
	num1=num2
	num2=num
	i += 1	
if (n == 1 or n ==2):
	num=1
print("斐波那契数列第%d个的数的值是：%d" % (n,num))


