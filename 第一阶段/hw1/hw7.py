# 7.输入三个整数x,y,z，请把这三个数由小到大输出。
print("请输入三个整数（用空格隔开）：")
a, b, c = map(int, input().split())
list1 = [a,b,c]
list1.sort()
print(list1[0],list1[1],list1[2])
