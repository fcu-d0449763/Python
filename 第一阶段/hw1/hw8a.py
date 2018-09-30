'''
a.根据n的值的不同，输出相应的形状
n = 5时             n = 4
*****               ****
****                ***
***                 **
**                  *
*
'''
number = int(input("请输入n的值:"))
while number > 0:
	newstr = '*' * number
	number -= 1
	print(newstr)

