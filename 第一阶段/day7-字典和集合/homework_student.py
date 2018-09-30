# @Author   :xaidc
# @Time     :2018/8/28 16:21
# @File     :homework_student.py
def menu():
    print('='*20)
    print("欢迎来到学生管理系统！！！")
    print('1.添加学生信息')
    print('2.查看学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.退出系统')
    print('='*20)

student = []
#添加学生信息
while True:
    menu()
    num = int(input('请输入选项（1~5）：'))
    if num == 1:
        print("你选择的是添加学生信息")
        name1 = input('请输入学生的姓名：')
        age1 = int(input('请输入学生的年龄：'))
        phone_num = int(input('请输入学生的电话号码：'))
        stu = {'name':name1,'age':age1,'phone_num':phone_num}
        student.append(stu)
        print("添加一名学生信息成功！！")

    #查看学生信息
    elif num == 2:
        print("你选择的是查看学生信息")
        if len(student) == 0:
            print("还没有学生信息被添加，请添加学生信息！！")
        else:
            print("姓名           年龄           电话号码")
            for i in student:
                print(i['name'],i['age'],i['phone_num'],sep='           ',end = '\n')

    #删除学生信息
    elif num == 3:
        print("你选择的是删除学生信息")

        if len(student) == 0:
            print("还没有学生信息被添加，请添加学生信息！！")
        else:
            print('='*20)
            name2 = input("请输入你要删除学生的姓名：")
            for item in student[:]:
                if item['name'] == name2:
                    student.remove(item)
                    print("该学生已删除")
                    break

    #修改学生信息
    elif num == 4:
        print("你选择的是修改学生信息")
        name3 = input('请输入你想修改学生的姓名')
        for item in student[:]:
            if item['name'] == name3:
                name4 = input("请输入修改后的学生姓名：")
                age2 = int(input('请输入修改后学生的年龄：'))
                phone_num1 = int(input('请输入修改后的学生的电话号码：'))
                new_stu = {'name':name4,'age':age2,'phone_num':phone_num1}
                item.update(new_stu)
                print('修改学生信息成功！！')
    elif num == 5:
        print('已退出学生管理系统')
        break
    else:
        print('你输入的格式不对，请按要求输入！')



