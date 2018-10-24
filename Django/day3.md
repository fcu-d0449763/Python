### 1.一对一
举例:  
1.在已经创建好的student表中添加两个字段
```
# 定义 Chinese字段,语文成绩
chinese = models.DecimalField(decimal_places=1,max_digits=4,null=True)
# 定于math字段,数学成绩
math = models.DecimalField(decimal_places=1, max_digits=4, null=True)
```
2.新增一个表,并在表中指定和哪个表一对一关联关系
```
class StudentInfo(models.Model):
    phone = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=100)
    # OneToOneField 指定一对一关联关系,该字段定义在任何一个模型都可以
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'student_info'
```
##### 通过student表查询扩展表的信息
```
def sel_info_by_stu(request):
    if request.method == 'GET':
        # 通过学生查询扩展表信息
        stu = Student.objects.get(s_name='小江')
        # 第一种
        # info = StudentInfo.objects.filter(stu_id=stu.id)
        # info = StudentInfo.objects.filter(stu=stu).first()
        # 第二种,学生对象,关联的模型名的小写
        info = stu.studentinfo
        print(info.address)
```
##### 通过扩展表信息查询学生表信息
```
def sel_stu_by_info(request):
    if request.method == 'GET':
        # 知道手机号码,找人
        info = StudentInfo.objects.get(phone='15008360363')
        student = info.stu
        print(student.s_name)
        return HttpResponse('通过手机号码查找学生的信息')
```
### 2.一对多
举例:  

1.新建一个表,名为grade
```
class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'grade'
```
2.在student表中再添加一个外键
```
grade = models.ForeignKey(Grade,null=True)
```
3.在grade表中添加几条数据
```
def add_grade(request):
    if request.method == 'GET':
        Grade.objects.create(g_name='软工一班')
        Grade.objects.create(g_name='软工二班')
        Grade.objects.create(g_name='软工三班')
        Grade.objects.create(g_name='空信一班')
        Grade.objects.create(g_name='空信二班')
```
4.查询信息
```
def sel_stu_grade(request):
    if request.method == 'GET':
        # 1.通过学生查找班级
        stu = Student.objects.filter(s_name='小明').first()
        grade = stu.grade
        print(grade.g_name)
        # 2.通过班级查找学生
        grade = Grade.objects.get(g_name='软工一班')
        students = grade.student_set.all()
        for stu in students:
            print(stu.s_name)

        return HttpResponse('查询学生和班级信息')
```
### 3.查询student表中的信息,并在网页上显示出来
1.在项目文件夹下创建一个名为templates文件夹,用来存放网页文件  
2.在settings.py文件中修改一下内容,(上下分别有两个空行)
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
3.获取student信息

```
def all_stu(request):
    # 获取所有学生信息
    stus = Student.objects.all()
    # 返回页面
    return render(request,'stus.html',{'students':stus})
```

4.在templates文件夹中创建一个stus.html文件
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table>
    <thead>
        <th>姓名</th>
        <th>年龄</th>
        <th>操作</th>
    </thead>
    <tbody>
        {% for stu in students%}
            <tr>
                <td>{{ stu.s_name }}</td>
                <td>{{ stu.s_age }}</td>
                <td>
                    <a href="/add_info/?stu_id={{ stu.id  }}"> 添加扩展信息</a>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
</body>
</html>
```
5.还可以在页面上操作,向数据库中添加数据

添加信息方法:
```
def add_info(request):
    # method 获取请求HTTP方式
    if request.method == 'GET':
        return render(request,'info.html')

    if request.method == 'POST':
        # 获取页面中提交的手机号码和地址,并保存
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        stu_id = request.GET.get('stu_id')
        #保存
        StudentInfo.objects.create(phone=phone,
                                   address=address,
                                   stu_id=stu_id)

        return HttpResponse('创建扩展表信息成功')
```

在templates文件夹下创建一个info.html文件

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="" method="post">
        电话号码:<input type="text" name="phone">
        地址:<input type="text" name="address">
        <input type="submit" value="提交">
    </form>
</body>
</html>
```


