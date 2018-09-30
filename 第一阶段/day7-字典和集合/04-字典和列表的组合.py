# @Author   :xaidc
# @Time     :2018/8/28 11:19
# @File     :04-字典和列表的组合.py

# 系统应该是一个容器：列表，字典
# 学生管理系统
# 1.一个系统可以存储多个学生
# 2.一个学生可以存储：姓名，电话，籍贯，专业，学号等等
# 3.添加学生
# 4.删除学生
# 5.修改学生的信息
# ...
# 什么时候使用列表？什么时候使用字典？
# 1.保存的多个数据是一个类型时候，用列表
# 例如：声明一个变量保存所有的数学成绩，声明一个变量保存所有的学生信息

# 2.保存的多个数据的类型不同，就使用字典
# 声明一个变量保存一个学生的信息，

student_system = [
    {'name':'stu1' ,'age':18 ,'tel':100,'native':'重庆'},
    {'name':'stu2' ,'age':19 ,'tel':110,'native':'北京'}
]
# 取出第一个学生的籍贯
print(student_system[0]['native'])

# 2.字典中有列表
py_class = {
    'class_name':'python1806',
    'student':[
    {'name':'stu1','age':12,'num':1},
    {'name':'stu2','age':13,'num':2}
    ]
}
print(py_class['student'][1]['name'])


# 练习：在班级Python1806添加一个学生，学生的信息自己输入，名字，年龄和id
# name = input("请输入名字：")
# age = int(input("请输入年龄："))
# num = int(input("请输入学号:"))
# stu = {'name':name,'age':age,'num':num}
# py_class['student'].append(stu)
# print(py_class)

# 练习：输入一个学生的姓名，根据姓名取删除对应的学生

name1 = input("请输入你想删除学生的姓名：")
# 获取班级上所有的学生
all_student = py_class['student']
for stu in all_student[:]:
    if stu['name'] ==name1:
        all_student.remove(stu)

print(py_class)


