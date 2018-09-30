'''
b.根据n的值的不同，输出相应的形状(n为奇数)
n = 5               n = 7
  *                    *
 ***                  ***
*****                *****
                    *******
'''
number = int(input("请输入一个奇数："))
n = 1
while n <= number:
	newstr = '*' * n
	n += 2
	print(newstr.center(number))
