# @Author   :xaidc
# @Time     :2018/9/3 18:48
# @File     :homework.py
import json
import random
# 1. 提取data.json中的数据，将每条数据中的name、text、love和comment信息。
# 并且保存到另外一个json文件中
# data2 = []
#
# with open('./files/data.json','r',encoding='utf-8') as f:
#     content = json.load(f)
#     print(content)
#
# for item in content["data"][:]:
#     data1 = {}
#     data1["name"] = item["name"]
#     data1["text"] = item["text"]
#     data1["comment"] = item["comment"]
#     data1["love"] = item["love"]
#     data2.append(data1)
#
#
# with open("./files/newdata.json",'w',encoding='utf-8') as ff:
#     json.dump(data2,ff,ensure_ascii=False,indent=2)
#     print(data2)

# 2. 统计data.json中comment数量超过1000的个数
# with open("./files/newdata.json",'r',encoding='utf-8') as f:
#     content = json.load(f)
# count = 0
# for item in data2:
#     if int(item["comment"]) > 1000:
#         count +=1
# print(count)


# 3. 将data.json文件中所有点赞数(love)对应的值超出1000的用k来表示，
# 例如1000修改为1k, 1345修改为1.3k

# with open("./files/data.json",'r',encoding='utf-8') as f:
#     content = json.load(f)
# for item in content["data"][:]:
#     if int(item["love"]) >= 1000:
#         item["love"]= str((int(item["love"])//100)/10) + 'k'
# with open('./files/newdata1.json','w',encoding='utf-8') as ff:
#     json.dump(content,ff,ensure_ascii=False,indent=2)
# print(content)


# 4. 写猜数字游戏，如果输入有误，提示重新输入，直达输入正确为止。
# 比如：输入数字的时候没有按要求输入，提示重新输入
# num = random.randint(1,100)
# while True:
#
#
#     try:
#         n = int(input("请输入数字"))
#         if n > num:
#             print ("大了，再小点！")
#         if n < num:
#             print ("小了，再大点！")
#         elif n == num:
#             print ("congradulation!!你猜对了")
#             break
#     except:
#         print ("输入错误，请重新输入")

# 5. 写学生管理系统的添加学生功能(数据需要本地化)，
# 要求除了保存学生的基本信息以外还要保存学生的学号，但是学号需要自动生成，生成原则：
# 添加第一个学生对应的学号是:py001
# 第二次添加的学生的学号是:py002
# ...
# 如果前面的学生因为各种原因被移除了，那后面添加学生的时候原则不变，
# 就是比如上次已经添加到py012,那么前面不管有没有删除情况，再次添加学生的学号是py013

# student = {"num":num,"name":name,"sex":sex,"phone_num":phone_num}
n=0
while True:
    with open('./files/add_student.json', 'r', encoding='utf-8') as f:
        content = json.load(f)


    name = input("请输入姓名：")
    sex = input("请输入性别:")
    phone_num = input("请输入电话号码：")
    num = 'py00' + str(n)
    n += 1
    student = {"num": num, "name": name, "sex": sex, "phone_num": phone_num}
    content.append(student)
    with open('./files/add_student.json', 'w', encoding='utf-8') as f:
        json.dump(content, f,ensure_ascii=False,indent=2)
