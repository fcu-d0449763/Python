# @Author   :xaidc
# @Time     :2018/8/31 15:38
# @File     :05-文件操作.py
'''
1.
程序中不管操作任何文件，不管怎么操作，过程都是：打开文件->操作（读/写）->关闭文件
2.
做数据持久化，本地化都要使用文件来保存数据
（数据库文件，txt文档，json文件，plist文件，xml文件等，二进制文件（图片，视频，音频等））

 程序中通过变量，列表，字典等保存的数据，在程序结束后都会被销毁的。
'''

"""
1.打开文件
open(文件地址，打开方式，encoding = 编码方式)
a.文件地址：告诉open函数要打开哪个文件，填文件路径。可以填绝对路径，也可以填相对路径
    绝对地址：一般不用
    相对地址：./相对路径（相对于当前文件所在的目录）
            ../相对路径（相当于当前文件所在的目录的上一层目录）
            .../相对路径（相当于当前文件所在的目录的上一层目录的上一层目录）
b.打开方式：获取文件的内容以读的形式打开，在文件中写内容就以写的形式打开
'r' -->读（默认值）,读出来的内容以文本的形式返回
'rb'/'br' --> 读，读出来的内容以二进制(bytes)的形式返回
'w' --->写，写文本到文件中
'wb'/'bw'--->写，写二进制数据到文件中
'a'--->写，追加

c.编码方式：以文本的形式读和写的时候才需要设置编码方式。
utf-8:万国码
gbk：只支持中文

d.open函数的返回值是被打开的文件对象


2.关闭文件
文件对象.close()
"""
# 1.打开文件
# f1 = open('D:/aaa.txt',encoding='utf-8')
# f2 = open('./test.txt','w',encoding='utf-8')

# 2.关闭文件
# f1.close()
# f2.close()

# 3.操作文件
# a. 读操作
# 打开文件，f就是被打开文件对象
f = open('./test.txt','r',encoding='utf-8')
# 获取文件中的所有内容，将结果返回给content保存
# 从文件开始读到第二行结束
content=f.readline()
print(content)
print('=====')
# 从第二行开始，读到第二行结束
print(f.readline())
print('====')

#从第三行开始，读到文件结束
print(f.read())
f.close()


# 练习，读文件中的内容，一行一行的读，读完为止
# f3 = open('D:/aaa.txt','r',encoding='utf-8')
# content = f3.readline()
# while content:
#     print("line:",content)
#     content = f.readline()
# f.close()

# b.写操作
'''
'w'--->写操作，完全覆盖原文件的内容
'a'--->写操作，在原文件的内容后去追加新的内容
'''
f = open('./test.txt','a',encoding='utf-8')
f.write("程序员的诗")
f.close()


# 4.文件不存在的情况
'''
当以读的形式打开文件的时候，如果文件不存在，程序会崩溃。会报错
当以写的形式打开一个不存在的文件的时候，会自动创建一个新的文件
'''

f = open('./test1.txt','w',encoding='utf-8')
f.write("你好，江秀成")
f.close()

# 练习:统计一个模块执行的次数
f = open('./test2.txt','r',encoding='utf-8')
number = int(f.read())
print(number)
f.close()
number +=1
f = open('./test2.txt','w',encoding='utf-8')
f.write(str(number))
f.close()