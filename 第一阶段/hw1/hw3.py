#3.求1+2!+3!+...+20!的和 1.程序分析：此程序只是把累加变成了累乘。
n = int(input("请输入你想求前多少项的和："))
count = 0
for j in range(1,n+1):
	num = 1
	for i in range(1,j+1):
		num *= i
	else:
		count += num
print("前%d项的和为%d" %(n,count))
