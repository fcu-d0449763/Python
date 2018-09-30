'''
有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个
分数。分子：上一个分数的分子加分母，分母：上一个分数的分子。
fz=2  fm = 1  fz+fm/fz
'''
fz = 2
fm = 1
fm1 = 0
n=int(input("请输入你想要第几个数："))
for i in range(1,n):
	fm1 = fz +fm
	fm = fz 
	fz=fm1
if n==1:
	fz = 2
	fm = 1
print("这个数列第%d个是：%d/%d"%(n,fz,fm) )



