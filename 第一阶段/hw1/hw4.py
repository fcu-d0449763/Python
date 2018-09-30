# 4.计算 1+1/2!+1/3!+1/4!+...1/20!=?
n = int(input("请输入你想求前多少项的和："))
count = 0
for j in range(1,n+1):
	num = 1
	for i in range(1,j+1):
		num *= i
	num1 = 1/num
	count += num1
print("前%d项的和为%.10f" %(n,count))
