# @Author   :xaidc
# @Time     :2018/9/5 15:45
# @File     :student_system.py
import file_manager
user_name = ''
# =========================添加学生=======

"""
一个账户对应管理不同的学生---不同的用户对应不同的json文件
json文件中的格式：
{
    'name':'',
    'number':个数,
    'all_students':[
        {'name':,'age':,'tel':,'id':}
    ]

}
"""
key_number = 'number'
key_all_students = 'all_students'
key_name = 'name'
key_age = 'age'
key_tel = 'tel'
key_id = 'id'
def get_system_info():
    """获取系统文件内容"""
    system_info = file_manager.read_json_file(user_name+'.json')
    if system_info:
        return system_info
    return {}
def creat_id():
    """产生学号"""
    system_info = get_system_info()
    number = system_info.get(key_number,0)
    number += 1
    id = 'stu' + str(number).rjust(4,'0')
    return id,number



def add_student():
    while  True:

        # 1.输入信息
        name = input('姓名：')
        age = input('年龄：')
        tel = input('电话：')
        # 2.产生id
        id, number = creat_id()

        # 3.创建学生
        stu = {key_name: name, key_age: age, key_tel: tel, key_id: id}

        # 4.保存学生信息
        system_info = get_system_info()
        all_student = system_info.get(key_all_students,[])
        all_student.append(stu)
        # 5.保存到文件中
        system_info[key_all_students] = all_student
        system_info[key_number] = number
        re = file_manager.write_json_file(user_name + '.json', system_info)
        if re:
            print('添加成功！')
        else:
            print('添加失败')

        print('1.继续添加')
        print('2.返回')
        value = input('请选择（1/2):')
        if value == '1':
            continue
        else:
            break
#===================查找学生==============
def find_student():
    all_students = get_system_info().get(key_all_students,[])
    if not all_students:
        print('目前还没有学生！')
        return
    print('1.查看所有的学生')
    print('2.根据姓名查找学生')
    print('3.根据学号查找学生')
    value = input('请选择（1-3）：')

    if value == '1':
        for stu in all_students:
            print('姓名：%s 学号：%s 年龄：%s 电话：%s'%(stu[key_name],stu[key_id],stu[key_age],stu[key_tel]))
    if value == '2':
        name = input('姓名：')
        for stu in all_students:
            if stu[key_name] == name:
                print('姓名：%s 学号：%s 年龄：%s 电话：%s' % (stu[key_name], stu[key_id], stu[key_age], stu[key_tel]))
                break
        else:
            print('没有该学生！！')
    if value == '3':
        id = input('学号：')
        for stu in all_students:
            if stu[key_id] == id:
                print('姓名：%s 学号：%s 年龄：%s 电话：%s' % (stu[key_name], stu[key_id], stu[key_age], stu[key_tel]))
                break
        else:
            print('没有该学生！')
#=================================删除学生============================
def delete_student():
    print('1.按姓名删除学生')
    print('2.按学号删除学生')
    system_info = get_system_info()
    all_students = get_system_info().get(key_all_students,[])
    if not all_students:
        print('目前还没有学生！')
        return
    value = input('请选择（1-2）：')
    if value == '1':
        name = input('请输入你要删除学生的姓名：')
        for stu in all_students[:]:
            if stu[key_name] == name:
                all_students.remove(stu)
                print('该学生已删除')
                break
        system_info[key_all_students] = all_students
        file_manager.write_json_file(user_name+'.json',system_info)
    elif value == '2':
        id = input('请输入你要删除学生的学号：')
        for stu in all_students[:]:
            if stu[key_id] == id:
                all_students.remove(stu)
                print('该学生已删除')
                break
        system_info[key_all_students] = all_students
        file_manager.write_json_file(user_name+'.json',system_info)

def revise_student():
    print('1.按姓名修改学生')
    print('2.按学号修改学生')
    system_info = get_system_info()
    all_students = get_system_info().get(key_all_students, [])
    if not all_students:
        print('目前还没有学生！')
        return
    value = input('请选择（1-2）：')
    if value == '1':
        name = input('请输入你要修改学生的姓名：')
        for stu in all_students[:]:
            if stu[key_name] == name:
                age = input('年龄：')
                tel = input('电话：')
                stu[key_age] = age
                stu[key_tel] = tel
                print('修改学生信息成功')
        system_info[key_all_students] = all_students
        file_manager.write_json_file(user_name + '.json', system_info)
    if value == '2':
        id = input('请输入你要修改学生的学号：')
        for stu in all_students[:]:
            if stu[key_id] == id:
                name = input('名字：')
                age = input('年龄：')
                tel = input('电话：')
                stu[key_name] = name
                stu[key_age] = age
                stu[key_tel] = tel
                print('修改学生信息成功')
        system_info[key_all_students] = all_students
        file_manager.write_json_file(user_name + '.json', system_info)

# ==========================主页=========
def main_page():
    while True:
        print(file_manager.read_text_file('system.txt'))
        value = input('请选择（1-5）：')

        if value == '5':
            break
        elif value == '1':
            add_student()

        elif value == '2':
            find_student()


        elif value == '3':
            delete_student()


        elif value == '4':
            revise_student()

        else:
            print('输入有误，重新输入')

