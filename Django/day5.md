#### 1.重定向
```
# 5.1 重定向
def index_redirect(request):
    if request.method == 'GET':
        # 实现重定向到index方法上去
        # HttpResponse() 响应
        # render() 页面渲染
        # 第一种重定向,地址是硬编码
        # return HttpResponseRedirect('/app/index/')

        # from django.urls import reverse
        # 第二种重定向,使用反向解析reverse('namespace:name')
        return HttpResponseRedirect(reverse('dy:all'))
```
---
## 登录注册页面
#### 1.注册
注册方法
```
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        # 用于创建用户
        # 1.获取参数
        name = request.POST.get('name')
        password = request.POST.get('pw')
        password2 = request.POST.get('pw2')
        # 2.校验参数是否完整  all()方法
        if not all([name,password,password2]):
            msg = '请填写完整'
            return render(request,'register.html',{'msg':msg})
        # 3.先判断数据库中是否存在该name用户
        if User.objects.filter(name=name).first():
            msg = '该账号已注册,请去登录'
            return render(request, 'register.html', {'msg': msg})

        # 4.校验密码是否一致
        if password != password2:
            msg = '两次密码不一致,请重新输入'
            return render(request, 'register.html', {'msg': msg})

        # 5.注册
        User.objects.create(name=name,password=password)
        return HttpResponseRedirect(reverse('user:login'))
```
注册页面
```

{% extends 'base.html' %}

{% block title %}
    注册页面
{% endblock %}


{% block content %}

<form action="" method="post">
    <table>
        <thead>
            <th>用户名</th>
            <th>密码</th>
            <th>确认密码</th>
        </thead>
        <tbody>
            <tr>
                <td>
                    <input type="text" name="name">
                </td>
                <td>
                    <input type="text" name="pw">
                </td>
                <td>
                    <input type="password" name="pw2">
                </td>
                <td>
                    <input type="submit" value="提交">
                </td>
            </tr>
        </tbody>
    </table>
    {{ msg }}
</form>

{% endblock %}
```
#### 2.登录
登录方法
```
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        # 1.获取参数
        name = request.POST.get('name')
        password = request.POST.get('pw')
        # 2.验证数据完整性
        if not all([name,password]):
            msg = '请填写完整的登录信息'
            return render(request,'login.html',{'msg':msg})

        # 3.验证用户是否注册
        user = User.objects.filter(name=name).first()
        if not user :
            msg = '该账号没有注册,请去注册'
            return render(request,'login.html',{'msg':msg})

        # 4.校验密码
        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})

        # 重点
        # 请求: 请求是从浏览器发送请求的时候,传递给后端的.
        # 响应: 后端返回给浏览器的

        res = HttpResponseRedirect(reverse('user:index'))
        # set_cookie(key,value,max_age)
        token = ''
        s = '1234567890qwertyuiopasdfghjklzxcvbnm'
        for i in range(25):
            token += random.choice(s)
        res.set_cookie('token',token,max_age=6000)

        # 存token值
        user_token = UserToken.objects.filter(user=user).first()
        if not user_token:
            UserToken.objects.create(token=token,user=user)
        else:
            user_token.token = token
            user_token.save()
        return  res
```
登录页面
```
{% extends 'base.html' %}
{% block title%}
    登录页面
{% endblock %}

{% block content %}
<form action="" method="post">
    用户名<input type="text" name="name">
    密码<input type="password" name="pw">
    <input type="submit" value="登录">
</form>
{{ msg }}
{% endblock %}
```
#### 3.主页
```
@login_required
def index(request):
    if request.method == 'GET':
        # token = request.COOKIES.get('token')
        # # 查询标识符是否有效
        # user_token = UserToken.objects.filter(token=token).first()
        # if not user_token:
        #     # 查询不到信息,说明用户没有登录
        #     return  HttpResponseRedirect(reverse('user:login'))
        return render(request,'index.html')
```
装饰器
```
def login_required(func):

    def check_login(request):
        # func 是被login_required装饰的函数
        token = request.COOKIES.get('token')
        if not token:
            # cookie 中没有登录的标识符,跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token 标识符有误,跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))

        return  func(request)

    return check_login
```
#### 4.注销
```
@login_required
def logout(request):
    if request.method == 'GET':
        # 1.删除cookie
        res = HttpResponseRedirect( reverse('user:login'))
        res.delete_cookie('token')
        # 2.删除UserToken中的数据
        token = request.COOKIES.get('token')
        UserToken.objects.filter(token=token).delete()

        return res
```
#### 5.重点
**cookie**+**session**  
1.cookie
>HTTP协议是无状态的.因此,若不借助其他手段,远程的服务器就无法知道以前和客户端做了哪些通信.Cookie就是其他手段之一.Cookie一个典型的应用场景,就是用于记录用户在网站上的登录状态

2.cookie方法
>设置：response.set_cookie(key, value, max_age=None, exprise=None)  
>获取：request.GET.get(key)  
>删除：request.delete_cookie(key)

eg
```
token = ''
        s = '1234567890qwertyuiopasdfghjklzxcvbnm'
        for i in range(25):
            token += random.choice(s)
        res.set_cookie('token',token,max_age=6000)
```

3.删除cookie  
eg
```
UserToken.objects.filter(token=token).delete()
```
