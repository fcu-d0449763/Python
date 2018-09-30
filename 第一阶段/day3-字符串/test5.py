#endswith(suffix, beg=0, end=len(string))
num1='jiangxiucheng'
num2='ng'
print(num1.endswith(num2,1,3))
print(num1.endswith(num2,1,5))


#find(str, beg=0 end=len(string))检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
num3='ch'
print(num1.find(num3))


#isalnum()如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
print(num1.isalnum())


#7	max(str)返回字符串 str 中最大的字母。
print(max(num1))