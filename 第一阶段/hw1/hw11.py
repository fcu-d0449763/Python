'''
11.我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，
题意是这样的： 5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。
现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。
'''
boy_chicken = 5
girl_chicken = 3
child_chicken = 1/3
for i in range(20):
	for j in range(33):
		x = 100 - i - j
		if boy_chicken*i + girl_chicken*j +child_chicken*x ==100:
			print("公鸡有%d只，母鸡有%d只，雏鸡有%d只"%(i,j,x))
