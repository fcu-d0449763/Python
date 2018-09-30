def hello():
	print("hello world!")
hello()



def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print( b ) # 结果是 2



# 可写函数说明
def printinfo( arg1, *vartuple ):#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)