'''
打印出所有的水仙花数，所谓水仙花数是指一个三位数。其各位数字立方和等于

该数本身。例如153就是一个水仙花数，因为153=1^3+5^3+3^3
'''

num = 0
for i in range(100,1000):
	newstr=str(i)
	if (i ==int((newstr[0]))**3+int((newstr[1]))**3+int((newstr[2]))**3):
		print(newstr)
		num += 1
print("一共有%d个三位数是水仙花数"%num)