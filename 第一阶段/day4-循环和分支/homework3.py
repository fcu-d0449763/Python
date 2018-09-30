'''
2.判断101-200之间有多少个素数，并输出所有素数。
判断素数的方法在；用一个数分别除2到sqrt（这个数），
如果能被整除，则表明次数不是素数，反之是素数。
'''

import math
num = 0
for i in range(101,201):
	for x in range(2,int(math.sqrt(i))+1):
		if i%x == 0:
			break
	else:
		print(i)
		num += 1		
print('101-200之间有%d个素数'% num)

