#  进制

# 计算机中常用的进制有：二进制，八进制，十进制，十六进制
# 十进制：
# 1.基数：0,1,2,3,4,5,6,7,8,9
# 2.进位：逢10进1
# 3.十进制上的每一位：

# 二进制
# 1.基数：0,1
# 2.进位：逢二进一  

# 八进制
# 1.基数：0,1,2,3,4,5,6,7
# 2.进位：逢8进1

# 十六进制
# 1.基数：0,1，2,3，4,5,6,7,8,9，a-f   
# 2.进位：逢十六进一


# 进制间的转换
# 1.二进制，八进制，十六进制--->十进制

# 2.八进制，十六进制--->二进制
# 将一位的八进制转换成3位的二进制。将一位的十六进制转换为4位的二进制
# 123（8）->  001010011(2)
# 123(16) ->000100100011(2)

# 3.二进制--->八进制，十六进制
# 将三位的二进制转换为1位的八进制。将四位的二进制转换成一位的十六进制


# 4.十进制-->二进制
# 相除取余法


# Python对进制的支持
# Python支持整数的二进制，八进制，十进制，十六进制
#     1.Python中的二进制，八进制，十六进制的表示
#     二进制：0b
#     八进制:0o
#     十六进制：0x
# 例  print(bin(20))   将其他的数据转换成二进制    bin()
# 例  print(oct(20))   将其他的数据转换成八进制	  oct()
# 例  print(hex(20))   将其他的数据转换成十六进制  hex()

# 计算机在存数据的时候，都是以二进制的形式存在计算机中（存一个数的补码）
'''
1.原码：数据的二进制形式
正数的原码：符号位的值是0，后面的是数值大小
负数的原码：符号位的值是1，后面的是数值大小


2.反码
正数的反码：正数的反码和原码一样
负数的反码：符号位不变，后面的每一位的值取反

例：10：  原码：00001010，反码：00001010
    -10： 原码：10001010，反码：11110101


3.补码
正数的补码：补码和原码一样
负数的补码：反码+1
'''
#计算机只有加法器