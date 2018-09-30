#字符串的相关运算

#1.+ 运算符
# 字符串1+字符串2
# Python支持两个字符串相加，其效果就是将两个字符串拼接在一起产生一个新的字符串
# 注意：如果+的一个是字符串，那么另外一个也必须是字符串

print('abc'+'123')

#2.*运算符
'''
字符串*整数:字符串重复多次
'''
print('abc'*3)

#3.所有的比较运算符
str1='abc'
print('abc'==str1)

#比较大小
'''
str1 > str2；str1 < str2
让str1中的每一位的字符，分别和str2中的每一位的字符依次比较。直到不同为止，再看不同字符中谁的编码值大或者小
'''
print('abcd'>'ac')

#4. in 和 not in
'''
str1 in str2 :判断str1是否在str2中
结果是 布尔值
'''

print('abc' in 'abcd')
print('f' not in 'python')


#5.获取字符串长度
#字符串的长度，指的是字符串中字符的个数
#len()内置函数
str3='study'
print(len(str3))


#补充：空串
str4=''
print(len(str4))


#6.阻止转义
#在字符串的最前面添加r/R可以阻止转义
print('a\nb')
print(r'a\nb')

