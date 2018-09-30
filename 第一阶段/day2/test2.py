#python 基础语法


#1.注释（是不会参与代码的编译和执行的。只是对代码进行解释和说明的文字。）：
#单行注释就是在注释文字前加#
#1.
"""
这是多行注释
这是多行注释
"""
#2.
'''
这是多行注释
这是多行注释
'''


#2.标识符（专门用来命名的-变量，函数，类）
#a.是由字母数字下划线组成（只能少不能多）
#b.数字不能开头的
#c.大小写敏感的（大写和小写不一样）
#d.Python3以后，标识符可以包含非ASCII码

# A.B.C  A-大版本，重大修改



#3.关键字（保留字）
# import keyword
# print(keyword.kwlist)
#Python中保留用来作为特殊功能一些单词
'''
['False', 'None', 'True', 'and', 'as',
 'assert', 'break', 'class','continue', 'def', 
 'del', 'elif', 'else', 'except', 'finally',
  'for', 'from', 'global', 'if', 'import', 
  'in','is', 'lambda', 'nonlocal', 'not', 
  'or', 'pass', 'raise', 'return', 'try', 
  'while', 'with', 'yield']
'''


#4.行与缩进
#缩进的要求：
'''
A.同一级的代码必须保持同一缩进。（统一使用tab来产生缩进）
B.通过缩进来产生代码块（类似于其他语言中的{}）
'''
#行的规范
'''
a.声明函数的前后必须有两个换行
b.声明类的前后也需要两个换行
c.多个功能模块间用换行隔开
'''


#5.多行显示（一句代码多行显示）
#a.在换行的地方加\号，然后在后面换行。换行后随便加缩进。
#b.列表，字典，元组和集合的字面量换行不用加\


#6.字面量（具体的值）
# a.数字字面量：10,23
# b.布尔值：True,False
# c.字符串：'jiang'
# d.列表：[10,23,'jiang']
# e.字典：{'a':12,'jiang':'江'}


# 7.Python中的数据类型
# a.数字相关的：int（整型），float（浮点型），complex（复数）
# b.bool 布尔：只有True和False
# c.str（字符串）
# d.list(列表)
# e.dict(字典)
# f.tuple（元组）
# g.set（集合）
# h.function（函数）
# i.bytes(字节)