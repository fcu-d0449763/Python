# @Author   :xaidc
# @Time     :2018/9/1 8:29
# @File     :student.py
import os
def menu1():
    '''
    学生管理系统菜单
    :return:
    '''
    print('='*25)
    print("||欢迎来到学生管理系统!!! ||")
    print('||1.添加学生信息!        ||')
    print('||2.查看学生信息!        ||')
    print('||3.删除学生信息!        ||')
    print('||4.修改学生信息!        ||')
    print('||5.返回上一级！         ||')
    print('||6.退出系统!           ||')

    print('='*25)



def add_stu():
    '''
    向学生管理系统里面添加学生信息，学生信息包括姓名，年龄，电话号码
    :return:
    '''
    print('-'*25)
    print("你选择的是添加学生信息")
    while True:
        name1 = input('请输入学生的姓名：')
        age1 = int(input('请输入学生的年龄：'))
        phone_num = int(input('请输入学生的电话号码：'))
        f1 = open('./aaa.txt', 'r', encoding='utf-8')
        a = f1.read()
        student1 = eval(a)
        f1.close()
        stu = {'name': name1, 'age': age1, 'phone_num': phone_num}
        student = student1
        student.append(stu)
        f = open('./aaa.txt', 'w', encoding='utf-8')
        f.write(str(student))
        f.close()
        print("添加一名学生信息成功！！")
        n = input("是否继续添加学生信息？（Y/N）:")
        if n == 'N':
            break


def check_stu():
    '''
    查看学生信息管理系统里面存储的学生信息
    :return:
    '''
    print('-' * 25)
    print("你选择的是查看学生信息")
    if os.path.getsize('./aaa.txt') == 0:
        print("还没有学生信息被添加，请添加学生信息！！")
    else:
        print("姓名           年龄           电话号码")
        f1 = open('./aaa.txt', 'r', encoding='utf-8')
        a = f1.read()
        student1 = eval(a)
        f1.close()
        for i in student1:
            print(i['name'], i['age'], i['phone_num'], sep='           ', end='\n')



def del_stu():
    '''
    根据学生的姓名，从学生管理系统中删除该学生
    :return:
    '''
    print('-' * 25)
    print("你选择的是删除学生信息")
    while True:
        if os.path.getsize('./aaa.txt') == 0:
            print("还没有学生信息被添加，请添加学生信息！！")
        else:
            print('=' * 20)
            name2 = input("请输入你要删除学生的姓名：")
            f1 = open('./aaa.txt', 'r', encoding='utf-8')
            a = f1.read()
            student1 = eval(a)
            f1.close()
            for item in student1[:]:
                if item['name'] == name2:
                    student1.remove(item)
                    print("该学生已删除")
                    break
            f = open('./aaa.txt', 'w', encoding='utf-8')
            f.write(str(student1))
            f.close()
        n = input("是否继续删除学生信息？（Y/N）:")
        if n == 'N':
            break


def update_stu():
    '''
    根据学生的姓名修改学生的基本信息
    :return:
    '''
    print('-' * 25)
    print("你选择的是修改学生信息")
    while True:
        name3 = input('请输入你想修改学生的姓名')
        f1 = open('./aaa.txt', 'r', encoding='utf-8')
        a = f1.read()
        student1 = eval(a)
        f1.close()
        for item in student1[:]:
            if item['name'] == name3:
                name4 = input("请输入修改后的学生姓名：")
                age2 = int(input('请输入修改后学生的年龄：'))
                phone_num1 = int(input('请输入修改后的学生的电话号码：'))
                new_stu = {'name': name4, 'age': age2, 'phone_num': phone_num1}
                item.update(new_stu)
                print('修改学生信息成功！')
        f = open('./aaa.txt', 'w', encoding='utf-8')
        f.write(str(student1))
        f.close()
        n = input("是否继续修改学生信息？（Y/N）:")
        if n == 'N':
            break



def register():
    '''
    用户注册
    :return:
    '''
    while True:
        user_name = input("请输入用户名：")
        pwd = int(input("请输入密码："))
        f1 = open('./aaB.txt', 'r', encoding='utf-8')
        a = f1.read()
        user1 = eval(a)
        f1.close()
        users = {'user_name1':user_name,'pwd1':pwd}
        user = user1
        user.append(users)
        f = open('./aaB.txt', 'w', encoding='utf-8')
        f.write(str(user))
        f.close()
        print("注册成功！！")
        break


def old_user():
    '''
    用户登录
    :return:
    '''
    print('-'*25)
    print("请登录！")
    f1 = open('./aaB.txt', 'r', encoding='utf-8')
    a = f1.read()
    user = eval(a)
    f1.close()
    user_name = input("请输入用户名：")
    pwd = int(input("请输入密码："))
    for item in user:
        if item['user_name1'] == user_name:
            if item['pwd1'] == pwd:
                print('登录成功')
                break
            else:
                print('密码错误')
    else:
        print('不存在该用户！')





def menu2():
    print('='*25)
    print('请登录或者注册学生管理系统')
    print('1.注册！')
    print('2.登录！')
    print('3.退出！')

def mangement():

    while True:
        menu1()
        num = int(input('请输入选项（1~5）：'))
        if num == 1:

            add_stu()
        elif num == 2:
            check_stu()
        elif num == 3:

            del_stu()
        elif num == 4:

            update_stu()
        elif num == 5:
            break
        elif num == 6:
            print('已退出学生管理系统')
            break

        else:
            print('你输入的格式不对，请按要求输入！')




student=[]
user = []
x = 1
while True:
    menu2()
    num1  = int(input("请输入选项（1~3）："))
    if num1 == 1:
        register()
        continue
    elif num1 == 2:
        old_user()
    # /////////
    elif num1 ==3:
        break
    mangement()








