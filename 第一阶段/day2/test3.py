#变量
#Python是动态语言

#声明变量就是在内存中开辟空间存储数据（变量就是用来存储数据的）

#1.怎么声明变量
#格式：变量名=值
#说明：
'''
类型：Python声明变量的时候不需要确定类型
变量名：标识符，不能是关键字；见名知义，PEP8命名规范（所有的字母都小写，多个单词之间用下划线_隔开）
=：赋值符号，将右边的值赋给左边变量
值：表达式（就是有结果的，例如：字面量，运算表达式（19+23），其他的变量）

'''
#声明了一个变量name，赋值为'路飞'。使用name的时候，就相当于在使用'路飞'
#name='路飞'
#print(name)

#声明一个变量class_name,保存'Python1806'
#class_name='Python1806'     #驼峰式：className
#num=100

#如果声明一个变量，可以存储不同类型的数据
#num='娜美'

#2
#num1=12；num2=13   python中每条语句结束可以不用分号。但是如果一行要写多条语句，就必须加分号 
#str1=str2='abc'    同时声明两个变量，并且赋一样的值
#print（str1，str2，str3）  使用print同时打印多个值


#3.id函数
#id（变量）---查看变量的地址
#python 声明变量，和给变量赋值的原理：先在内存内开辟空间存数据，然后再将变量名作为数据对应的内存的标签
#eg
i=10
print(id(i))
i=100
print(id(i))











