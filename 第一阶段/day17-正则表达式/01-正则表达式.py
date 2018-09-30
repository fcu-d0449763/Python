# @Author   :xaidc
# @Time     :2018/9/11 8:52
# @File     :01-正则表达式.py
from re import fullmatch,findall

'''
正则表达式就是用来检测字符串是否满足某种规则的工具
例如:1.账号是手机号/邮箱/多少位由什么组成等...
    2.可厉害奇偶is发到空间撒个,弄iu闪避授课计划如何.好搜和好贵is和oil看?
    3.脏话替换成*等....


1.正则语法
2.python对正则表达式的支持,提供了了一个内置模块:re
fullmatch(正则表达式,字符串):判断整个字符串是否符合正则表达式规则


'''
# ============================单个字符=================
# 1) . 匹配任意字符
# 匹配一个字符串,只有一位字符,并且这个字符是任意字符
re_str = r'.'
result = fullmatch(re_str,'an')
print(result)
# 匹配一个字符串,只有两位字符,并且每个字符是任意字符
re_str = r'..'
result = fullmatch(re_str,'an')
print(result)
# 匹配一个字符串,前三位分别是abc,最后一位是任意字符
re_str = r'abc.'
result = fullmatch(re_str,'abcw')
print(result)

print('====================================')
# 2)\w 匹配 字母 数字 下划线
# 匹配一个字符串,前三位分别是abc,最后两位是字母数字下划线
re_str = r'abc\w\w'
result = fullmatch(re_str,'abc1_')
print(result)

print('===================================')
# 3) \s 匹配空白字符(空白指空格,制表符和回车等所有能产生空白的字符)
# 匹配一个字符串,前三位是字母数字下划线第四位是一个空白字符,最后一位是任意字符
re_str = r'\w\w\w\s.'
result = fullmatch(re_str,'h2_ 9')
print(result)
print('========================================')
# 4) \d 匹配一个数字字符
re_str = r'\d\d\d.'
result = fullmatch(re_str,'666j')
print(result)
print('========================================')
# 5) \b 检测是否是单词边界(单词的开头,单词的结尾,单词和单词之间的标点空格等)
#注意:正则中遇到\b,匹配的时候先不管他,匹配成功后再回头看\b位置是否是单词边界
# 匹配一个字符串是前四位是when,第五位是空白,空白后面是where,并且第四位n的后面是个边界
re_str = r'when\b\swhere'
result = fullmatch(re_str,'when where')
print(result)
print('=========================================')

# 6)^ 检测字符串是否以给定的正则表达式开头
re_str = r'^\d\d'
result = fullmatch(re_str,'23')
print(result)
print('=========================================')

# 7).$ 检测字符串是否以给定的正则表达式结束
# 匹配一个字符串a数字,并且a数字是字符串的结尾
re_str = r'a\d$'
result = fullmatch(re_str,'a2')
print(result)
print('======================================')

# 8) \W 匹配一个非字母,数字,下划线的字符
re_str = '\W\w'
result = fullmatch(re_str,'!a')
print(result)
print('====================')

# 9) \S 匹配非空白字符
re_str = r'\S\w\w\w'
result = fullmatch(re_str,'@123')
print(result)
print('====================================')
# 10) \D 匹配一个非数字字符
# 11) \B 检测非单词边界


# =========================匹配次数==============
# 1) [] 匹配中括号中出现的任意字符
# 注意:一个中括号只匹配一个字符
# 匹配一个三位的字符串,第一位是a或者b或者c,后两位是数字
re_str = r'[abc]\d\d'
result = fullmatch(re_str,'a67')
print(result)
print('============================')
# -(减)号 在正则中的中括号中的应用:如果将减号放到两个字符的中间代表的是谁是谁.如果想要表示'-'符号本身,就放在开头或结尾
# 要求一个字符串中的第一位是1到8中的一个,后面两位是小写字母
# [1-8]:代表的字符集是:12345678
# [-18]或者[18-]:代表的字符串是'-', '1', '8',和'1','8','-'
re_str = r'[1-8][a-z][a-z]'
result = fullmatch(re_str,'8jx')
print(result)
print('=============================')

# 2)[^字符集]匹配不在[]字符集中的任意一个字符
# 匹配一个四位的字符串,第一位不是大写字母,后三位是abc
re_str = r'[^A-Z]abc'
result = fullmatch(re_str,'aabc')
print(result)
print('=====================')

# 3) * 匹配0次或者多次
# 匹配一个字符串,最后一位是b,b的前面有0个或者多个a
re_str = r'a*b'   # 'b','ab','aab','aaab'
print(fullmatch(re_str,'b'))
print('===========================')

# 4) + 匹配1次或者多次(至少一次)
# 判断一个字符串是否是无符号的整数
re_str = r'[1-9]+\d*'
print(fullmatch(re_str,'001'))

# 5) ? 匹配0次或者一次
re_str = r'@?\d+'
print(fullmatch(re_str,'@6666'))

# 判断一个字符串是否是整数(包括正整数和负整数)
re_str = r'[+-]?[1-9]+\d*'
print(fullmatch(re_str,'200'))

# 6) {N} 匹配N次
# re_str = r'\d{3}'
re_str = r'[a-zA-Z]{3}'
print(fullmatch(re_str,'ahH'))

# 7) {N,} 至少匹配N次
re_str = r'\w{4,}'
print(fullmatch(re_str,'hahj123_sd'))
print('==========================')
# 8){,N}最多匹配N次
# 9){M,N}匹配至少M次,最多N次(N>M)
# 注意:次数相关的操作,都是约束的次数符号前的前一个字符


# =====================3.分支和分组========
# 1) | 分支(相当于逻辑运算中的or)
# 匹配一个字符串是三个字母或者是三个数字
re_str = r'[a-zA-Z]{3}|\d{3}'
print(fullmatch(re_str,'123'))

#注意: 正则中的分支有短路操作:如果使用|去连接多个条件,前面的条件已经匹配出结果,那么就不会使用后面的条件再去匹配了
# 练习:写一个正则表达式,能够匹配出字符串中所有的数字(包括整数和小数)

re_str = r'\d+[.]\d+|[1-9]\d*'
print(findall(re_str,'abc12.5hhh60,30.2kkk9nn0.12'))


#2)分组
# a.分组
# 通过加()来对正则条件进行分组
# 两位数字两位字母出现三次
re_str = r'([a-z]{2}\d{2}){3}'
print(fullmatch(re_str,'ac23bn45hj34'))

# 匹配一个字符串,按照一个数字一个字母的规律出现一次或者多次
re_str = r'(\d[a-z])+'
print(fullmatch(re_str,'2a3a'))

#b.重复
# 可以通过\数字来重复匹配前面的括号中匹配的结果.数字的值代表前面的第几个分组
re_str = r'(\d{2}[A-Z])=\1'
print(fullmatch(re_str,'23B=23B'))

re_str = r'(\d{3})-(\w{2})\1\2'
print(fullmatch(re_str,'222-as222as'))

# c.捕获
# 按照完整的正则表达式去匹配,只捕获()中的内容.只有在findall中有效
re_str = r'a(\d{3})b'
print(fullmatch(re_str,'a786b'))
print(findall(re_str,'a786b'))










# 练习:
# 用户名必须由字母,数字或下划线,构成且长度在6-20个字符之间
# QQ号是5-12的数字且首位不能为0

user_name = input('请输入用户名(数字,字母下划线,6-20字符):')
num = input("请输入qq号(5-12):")
re_str = r'\w{6,20}'
re_str1 = r'[1-9]\d{4,11}'
result = fullmatch(re_str,user_name)
if result == None:
    print('用户名不合法')
else:
    print('用户名合法')
if fullmatch(re_str1,num):
    print('qq号合法')
else:
    print('qq号不合法')


if __name__ == '__main__':
    pass