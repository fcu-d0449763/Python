# @Author   :xaidc
# @Time     :2018/8/27 18:50
# @File     :homework.py
#
# 1.已知一个列表，求列表中心元素
#奇数
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[int((len(list1)-1)/2)])
#偶数
list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2[int(len(list2)/2)-1],list2[int(len(list2)/2)])
# 2.已知一个列表，求所有元素和
list3 = [1,2,3,4,5,6,7,8,9,10]
count = 0
for item in list3:
    count += item
print(count)
# 3.已知一个列表，输出所有下标是奇数的元素
list4 = [1,2,3,4,5,6,7,8,9,10]
list5 = []
for item in range(len(list4)):
    if item % 2 != 0:
        list5.append(list4[item])
print(list5)
# 4.已知一个列表，输出所有元素中，值为奇数的元素。
list6 = [1,2,3,4,5,6,7,8,9,10]
list7 = []
for item in list6:
    if item % 2 != 0:
        list7.append(item)
print(list7)
# 5.已知一个列表，将所有的元素乘以2。
list8 = [1,2,3,4,5,6,7,8,9,10]
list9 = []
for item in list8:
    item *= 2
    list9.append(item)
list8 = list9
print(list8)
# 6.已知一个列表，将所有元素加到第一个元素中。
list10 = [1,2,3,4,5,6,7,8,9,10]
count = 0
for item in list10:
    count += item
list10[0] = count
print(list10)

list10 = [1,2,3,4,5,6,7,8,9,10]
LIST1 = []
for item in list10:
    LIST1.append(item)
list10[0] = LIST1
print(list10)
# 7.已知一个列表A，将奇数位置元素存到B列表中，偶数元素存到C列表中。
A = [1,2,3,4,5,6,7,8,9,10]
B = []
C = []
for item in range(len(A)):
    if item % 2 ==0:
        C.append(A[item])
    else:
        B.append(A[item])
print(B,C)
# 8.把A列表的前5个元素复制到B列表中。
A = [1,2,3,4,5,6,7,8,9,10]
B = A[0:5].copy()
print(B)
# 9.有一个长度是10的列表，按递增排列，用户输入一个数，插入适当位置。
D = [1,3,5,6,12,25,36,78,100,110]
num = int(input("请输入一个数:"))
for i in range(10):
    if num > D[9]:
        D.append(num)
        break
    if D[i] < num < D[i+1]:
        D.insert(i+1,num)

print(D)

# 10.自己实现列表的count方法的功能。
E = [1,2,3,2,3,5,6,6,2]
print(E.count(2))
# 11.自己实现列表的extend方法的功能。
numbers = [1,2,1,3,45,1]
numbers.extend([100,200])
print(numbers)
# 12.自己实现列表的index方法
numbers = [1,2,1,3,45,1]
print(numbers.index(1))