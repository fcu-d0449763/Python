'''
6.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。 
1.程序分析：关键是计算出每一项的值。
'''
number1 = int(input("请输入你想几个数字相加："))
number2 = int(input("你想这个数字是由什么数字组成："))
count = 0
newstr = str(number2)
for j in range(1,number1+1):
	newstr1 = newstr*j
	count += int(newstr1)	


print("结果为：%d" % count)
