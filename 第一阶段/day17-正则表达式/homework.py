# @Author   :xaidc
# @Time     :2018/9/11 16:36
# @File     :homework.py
import re
'''
1. 写一个正则表达式判断一个字符串是否是ip地址  
规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255  
255.189.10.37   正确    
256.189.89.9    错误 
'''
'''
re_str = r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[0-9])[.]' \
         r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[0-9])[.]' \
         r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[0-9])[.]' \
         r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[0-9])'
ip = input("请输入ip地址:")
result = re.fullmatch(re_str,ip)
if result:
    print('ip地址合法')
else:
    print('ip地址不合法')
    
'''

# 2. 计算一个字符串中所有的数字的和
# 例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
'''
re_str = r'\d+[.]\d+|[1-9]\d*'
result = re.findall(re_str,'hello90abc 78sjh12.5')
count  = 0
for i in result:
    count += float(i)
print(count)
'''
# 3. 验证输入的内容只能是汉字
'''
re_str = r'[\u4e00-\u9fa5]*'
string = input("请输入内容:")
result = re.fullmatch(re_str,string)
if result:
    print('汉字')
else:
    print('有非汉字')

'''



# 4. 电话号码的验证
# re_str = r'(13|14|15|18|17)[0-9]{9}'
# num = input("请输入电话号码:")
# result = re.fullmatch(re_str,num)
# if result:
#     print("是电话号码!")
# else:
#     print("你输入的不是电话号码!")





# 5. 简单的身份证号的验证
re_str = r'[1-9]\d{9}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])(\d{4}|X)'
ID =    input("请输入身份证号:")
result = re.fullmatch(re_str,ID)
if result:
    print("身份证号正确")
else:
    print("身份证号错误")
