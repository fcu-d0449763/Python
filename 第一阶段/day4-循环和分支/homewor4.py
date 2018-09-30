'''
给一个正整数，要求：1.求他是几位数 2.逆序打印出各位数字
'''
n=int(input("请输入一个正整数："))
newstr=str(n)
print("这个正整数是%d位数"%len(newstr))
print(int(newstr[::-1]))
