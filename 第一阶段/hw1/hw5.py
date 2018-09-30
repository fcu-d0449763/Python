'''
5.循环输入大于0的数字进行累加
，直到输入的数字为0，就结束循环，并最后输出累加的结果。
'''
count = 0
while True:
	number = int(input("请输入数字："))
	if number:
		count += number
	elif number == 0 :
		print("你之前所输入的所有的数的和为：%d" % count)
		break

			