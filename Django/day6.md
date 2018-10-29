## 用Django实现登录注册
### 1.注册
在views.py文件写注册方法
```
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        data = request.POST
        # 校验form表单传递的参数
        form = UserRegisterForm(data)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=name,password=password)
            return  HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})
```
在user应用在创建一个forms.py文件  
注册时的数据校验放在forms.py中  
```
class UserRegisterForm(forms.Form):
    # 定义一个那么字段,设置name字段的最大值和最小值
    # required是否必填
    username = forms.CharField(max_length=10,min_length=2,required=True,
                           error_messages={
                               'required':'注册姓名必填',
                               'min_length':'账号不能短于两个字符',
                               'max_length':'账号不能长于十个字符',
                           })
    password = forms.CharField(max_length=30,required=True,
                         error_messages={'required':'密码必填'})
    password2 = forms.CharField(max_length=30,required=True,
                          error_messages={'required':'确认密码必填'})

    def clean(self):
        # 获取用户名,用于校验该用户是否已经注册
        name = self.cleaned_data.get('username')
        user = User.objects.filter(username = name).first()
        if user:
            raise forms.ValidationError({'username':'该账户已注册'})
        # 验证密码是否一致
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password':'密码不一致'})
        return self.cleaned_data
```
### 2.登录
登录方法
```
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        if form.is_valid():
            # 使用随机标识符也叫做签名token
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if user:
                # 登录,向request.user属性赋值,赋值为登录系统的用户对象
                # 1.向页面的cookie中设置sessionid值,(标识符)
                # 2.向django_session表中设置对应的标识符
                auth.login(request,user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request,'login.html',{'msg':'密码错误'})
        else:
            return render(request,'login.html',{'errors':form.errors})

```
forms.py
```
class UserLoginForm(forms.Form):
    # 定义一个那么字段,设置name字段的最大值和最小值
    # required是否必填
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '注册姓名必填',
                                   'min_length': '账号不能短于两个字符',
                                   'max_length': '账号不能长于十个字符',
                               })
    password = forms.CharField(max_length=30, required=True,
                         error_messages={'required': '密码必填'})

    def clean(self):
        user = User.objects.filter(username = self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'该账号没有注册,请去注册'})

        return self.cleaned_data
```
修饰器
```
<!--在用django自带的修饰器的时候需要导入-->
from django.contrib.auth.decorators import login_required
```
注意:在表单类中定义校验的字段是否为必填项即required参数的设置，以及长度的限制即max_length、min_length，以及错误信息的自定义error_messages。通过重构clean()方法实现用户名的检测等功能。


## 中间件
中间件:  
1.是一个轻量级,底层的插件,可以介入Django的请求和响应的过程(面向切面编程)  
2.中间件的本质就是一个python类  
注意:中间件是帮助我们在视图函数执行之前和执行之后都可以做的一些额外的操作,他本质就是一个自定义类,类中定义了几个方法,Django框架在请求的特定的时间去执行这些方法

### 举例
1.在settings.py中,加入我们自定义的两个中间件
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
    'utils.middleware.TestMiddleware',
    'utils.middleware.Test2Middleware',

]
```

2.在项目文件夹创建一个utils文件夹,并在里面创建两个文件,分别是
__init__.py,middleware.py

3.在middleware.py文件下写两个类
```
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):

    def process_request(self,request):

        print('process_request')
        # 继续执行视图函数
        return None

    def process_response(self,request,response):
        print('process_response')
        # 返回响应
        return response
class Test2Middleware(MiddlewareMixin):

    def process_request(self,request):

        print('process_request2')
        # 继续执行视图函数
        return None

    def process_response(self,request,response):
        print('process_response2')
        # 返回响应
        return response
```
输出结果为
```
process_request
process_request2
process_response2
process_response
```

4.每个之间减是一个独立的类,有以下几个方法
>1.process_request(self,request)  
>   执行时间在django接收到request之后,但未解析出以确定运行哪个视图函数view之前  
>2.process_view(self,request, view_func, view_args, view_kwargs)
>3.rocess_response(self, request, response)
>   该方法必须返回HTTPResponse对象,可以是原来的,也可以是修改后的
>调用时机在django执行完view函数并生成response之后,该中间件能修改response的内容,常见用途比如压缩内容,request是request对象,response是从view中返回的response对象
>4. process_exception(self, request, exception)
>5. process_template_response(self, request, response)
