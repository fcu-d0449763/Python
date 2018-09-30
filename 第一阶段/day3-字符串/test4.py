#字符串相关的方法
#Python 为字符串提供了很多的內建函数
#字符串.函数
#注意：这些所有的函数的功能都不会影响原来的字符串，而是产生一个新的字符串
#1.capitalize（）将字符串的第一个字符转换为大写

str1= 'abc'
newstr=str1.capitalize()
print(newstr)

#2.center(width,fillchar)
#让字符串变成width对应的长度，原内容居中，剩余的部分使用fillchar的值来填充
#width-整数；fillchar-任意字符
print('abc'.center(10,'x'))


#3.rjust(width,fillchar)
#让字符串变成width对应的长度，原内容靠右，剩余的部分使用fillcharf的值来填充


#4.count(str)
#判断str值在原字符串中出现的次数
print('abcccc'.count('c'))


#5.str1.join(str2)
#在str2中的每个字符串之间插入一个str1
print('1'.join('ccc'))


#6.str.replace(old,new)
#将str1中的old全部替换成new
new_str='sahbushjbsaahdsjudhs'.replace('h','=')
print(new_str)


