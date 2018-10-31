1.用户和组的关系:多对多   groups  
2.组和权限的关系:多对多   permissions  
3.用户和权限:多对多    user_permissions 
### 1.自定义创建权限
```
class MyUser(AbstractUser):
    # 扩展django自带的auth_user表,可以自定义新增的字段

    class Meta:
        # django 默认给每个模型初始化三个权限
        # 默认的是change,delete,add权限
        permissions = (
            ('add_my_user','新增用户权限'),
            ('change_my_user_username','修改用户名权限'),
            ('change_my_user_password','修改用户密码权限'),
            ('all_my_user','查看用户权限')
        )
```
在settings.py 添加设置
```
# 告诉django,User模型修改为自定义的User模型
AUTH_USER_MODEL = 'user.MyUser'
```
### 2.创建用户,并给权限
```
def add_user_permission(request):
    if request.method == 'GET':
        # 1.创建用户
        user = MyUser.objects.create_user(username='jj',password='123')
        # 2.指定刚创建,并分配给他权限(新增用户权限)
        permissions = Permission.objects.filter(codename__in=['add_my_user','all_my_user']).all()
        for permission in permissions:
            user.user_permissions.add(permission)
        # 3.删除刚创建的用户的新增用户权限
        # user.user_permission.remove('add_my_user')
        return HttpResponse('创建用户权限成功')
```
### 3.用户为'jj',且有权限才能访问的页面
```
@check_permissions
def index(request):
    # 用户名为jj用户,
    # 有查看用户列表权限,才能访问index函数,使用装饰器去写
    if request.method == 'GET':

        return render(request,'index.html')
```
装饰器
```
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from user.models import MyUser
from django.contrib.auth.models import Permission

# 1.外层函数内嵌内层函数
# 2.外层函数返回内层函数
# 3.内层函数调用外层函数的参数

def check_permissions(func):

    def check(request):
        user = MyUser.objects.filter(username='jj').first()
        # 验证权限
        user_perm = user.user_permissions.filter(codename='change_my_user_password').first()
        if user_perm:
            # 用户有列表权限,则继续访问被装饰器装饰的函数
            return func(request)
        else:
            return HttpResponse('用户没有查看列表权限,不能访问方法')


    return check
```
### 4.创建组,并赋予权限
```
def add_group_permission(request):
    if request.method == 'GET':
        # 创建超级管理员(所有权限),创建普通管理员 (修改/查看权限)
        group = Group.objects.create(name='审核组')

        ps = Permission.objects.filter(codename__in=['change_my_user_username',
                                                'change_my_user_password',
                                                'all_my_user']).all()
        # 给组添加权限
        for permission in ps:
            group.permissions.add(permission)

        return HttpResponse('创建组权限成功')
```
### 5.给jj用户分配审查组
```
def add_user_group(request):
    if request.method == 'GET':
        # 给jj用户分配审查组
        check_group = Group.objects.get(name='审核组')
        user = MyUser.objects.get(username='jj')

        # 分配组
        user.groups.add(check_group)

        return HttpResponse('用户分组成功')
```
### 6.在permission.html显示jj的权限
```
def show_user_permission(request):
    if request.method == 'GET':
        user = MyUser.objects.get(username='jj')
        return render(request,'permissions.html',{'user':user})
```
permission.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <!--通过用户查询组,组查询权限-->
    {{ user }}
    {% for permission in user.groups.all.0.permissions.all %}
        {{ permission.codename}}
    {% endfor %}
    <!--通过用户直接查找权限-->
    <br>
    {%for per in user.user_permissions.all %}
        {{ per.codename}}
    {% endfor %}
</body>
</html>
```
### 7.django自带的权限验证
先导入库
```
from django.contrib.auth.decorators import permission_required
```
```
@permission_required('user.change_my_user')
def new_index(request):
    if request.method == 'GET':

        return HttpResponse('需要权限才能查看')
```
### 8
>1.给用户添加某种权限:  
添加权限:  
user对象.user_permission.add(permission对象1, permission对象2)  
删除权限:  
ser对象.user_permission.remove(permission对象1, permission对象2)    
清空权限:  
user对象.user_permission.clear()

>2.创建组:  
group(组对象) =Group.objects.create(name='组名')  
组添加权限:  
group对象.permissions.add(permission对象1, permission对象2)  
删除权限:  
group对象.permissions.remove(permission对象1, permission对象2)  
清空权限:  
group对象.permissions.clear()  


>3.用户分配到组:  
添加权限:  
user(用户对象).groups.add(check_group(组对象))  
删除权限:  
user对象.groups.remove(groups对象1, groups对象2)  
清空权限:  
user对象.groups.clear()

>4.查询  
1.通过用户查询权限  
自己实现查询用户对应的权限方法:  
user.user_permission.all()  
user.groups.all()[0].permissions.all()  
djiango自带查询方法:  
user.get_group_permission()  
user.get_all_permission()  
>2.权限验证  
自己实现权限验证  
user.user_permission.filter(codename='xxx')  
user.groups.all()[0].permissions.filter(codename='xxx')  
django实现权限验证  
user.has_perm('名称.权限名')




