'''
1.控制台输入年龄，根据年龄输出不同的提示
(例如:老年人，青壮年，成年人，未成年，儿童)

'''


age = int(input("请输入年龄了(0~120)："))
if 0 <= age <13:
	print("儿童，小屁孩")
elif 13 <= age < 18:
	print("未成年")
elif 18 <= age < 30:
	print("成年人")
elif 30 <= age < 60:
	print("青壮年")
elif  60 <= age <120:
	print("老年人")
else:
	print("妖精")