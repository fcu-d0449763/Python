# @Author   :xaidc
# @Time     :2018/8/29 10:46
# @File     :04-函数的参数.py

'''
参数：声明函数的时候的参数列表中的参数叫形参；调用函数的时候，参数列表中的参数叫实参
传参：传参的过程就是使用实参给形参赋值的过程，一定要保证每个形参都要有值

# 实参
1.位置参数：传参的时候实参的位置和形参一一对应（第一个实参传给第一个形参，第二个实参传给第二个形参。。）
2.关键字参数:函数调用的时候通过形参名'形参名 = 实参'的形式来传参
'''

# 1.位置参数
def fun1(a,b,c):
    print(a,b,c)
fun1(10,'acd',True)

# 2.关键字参数
fun1(b='acd',c=True,a=10)

'''
3.参数的默认值
a.在声明函数的时候，可以参数赋默认值。（可以给所有的参数赋默认值，也可以给部分参数赋默认值）
给部分参数赋默认值的时候，要求有默认值得默认值的参数必须放到参数列表的最后
b.调用参数有默认值的函数的时候，有默认值的参数可以传参也可以不传
'''
# 3.1声明函数的时候每个参数都有默认值
def func2(a='abc',b=2,c=0):
    print(a,b,c)
# 所有的参数都不传参，全部使用默认值
func2()
# 给部分参数传参
func2(10)
func2(b='abc')

# 3.2 参数列表中，部分参数有默认值(有默认的必须放到后面)
def func3(a,b,c=20):
    print(a,b,c)
#没有默认值的参数必须传参，有默认值的参数可以传也可以不传
func3(1,2)


'''
4.不定个数参数
python 通过在形参名前加*，让这个形参变成一个元组，来让这个形参可以同时接受多个实参，多个包含0
'''
# 写一个函数，计算多个数的和
def sum2(*nums):
    # print(nums,type(nums))
    sum1 = 0
    for i in nums:
        sum1 += i
    print(sum1)
sum2(1,2,3)

# 写一个函数，统计指定班级中所有的学生的成绩
def class_info(class_name,*score):
    print(class_name,score)

class_info('python1806',78,23,45,43)

def class_info2(class_name,location,*score):
    print(class_name,location,score)
class_info2('python','地址',12,34,54,32)


'''
5.对参数的类型进行说明
Python不能直接约束一个变量的类型，但是可以通过说明，来提示用户调用函数的时候，参数的类型
'''

def func4(name:str,age:int):
    print(name,age)
func4()