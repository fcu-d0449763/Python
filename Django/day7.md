### 1.中间件(补充)
1.中间件的使用,避免重定向的操作,在做登录验证的的时候,屏蔽掉登录和注册的url,不需要做登录验证  
2.day5项目中使用中间件进行登录校验
```
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 做登录验证
        # func 是被login_required装饰的函数
        # 屏蔽掉登录和注册的url,不需要做登录验证
        not_check = ['/user/login/','/user/register/']
        path = request.path
        if path in not_check:
            # 不继续执行以下登录验证的代码,直接取执行视图函数
            return None

        token = request.COOKIES.get('token')
        if not token:
            # cookie 中没有登录的标识符,跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token 标识符有误,跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))

        # 给全局request对象修改user属性值,修改为当前登录系统用户
        request.user = user_token.user
        return None
```

### 2.上传文件(day07项目)
1.在modles.py创建表
```
class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
```
2.上传文件页面
```
{% extends 'base.html' %}


{% block content %}
<form action="" method="post" enctype="multipart/form-data">
    标题:<input type="text" name="title"><br>
    描述:<input type="text" name="desc"><br>
    图片:<input type="file" name="img"><br>
    <input type="submit" value="提交">
</form>


{% endblock %}
```
3.在views.py创建方法
```
def add_article(request):
    if request.method == "GET":
        return render(request,'articles.html')


    if request.method == 'POST':
        # 获取数据
        img = request.FILES.get('img') 
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # 创建文章
        Article.objects.create(img=img,
                               title=title,
                               desc=desc)
        return  HttpResponseRedirect('创建图片成功')
```
4.因为涉及上传图片,所有就需要在django中去设置
>1.安装Pillow库  
    ```
    pip install Pillow
    ```
>2.配置上传图片的路径  
在项目文件夹下创建一个media文件夹用于保存图片等文件,在settings.py文件下写入  
    ```
    MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    ```  
然后在urls.py 文件下设置media  
    ```
    # 将media文件夹解析为静态文件夹
    # django在dubug为True的情况下,就可以访问media文件夹下的内容
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
    ```
### 3.分页
1.分页方法
```
def articles(request):
    if request.method == 'GET':
        # 默认是显示第一页
        page = request.GET.get('page',1)
        # 查询所有文章对象,并进行分页
        articles = Article.objects.all()
        # 将所有文章进行分页,每一页最多三条数据
        paginator = Paginator(articles,3)
        # 获取哪一页的文章信息
        arts = paginator.page(page)
        return render(request,'arts.html',{'arts':arts})
```
2.分页页面显示
```
{% extends 'base.html' %}

{% block content %}
{% for art in  arts %}
    <P> 编号:{{ art.id }}标题:{{ art.title }}</P>

{% endfor %}
<br>
<p>
    {% if arts.has_previous %}
        <a href="{% url 'user:articles'%}?page={{arts.previous_page_number}}">上一页</a>
    {% endif %}
    {% for i in arts.paginator.page_range %}
        <a href="{% url 'user:articles'%}?page={{ i }}">{{ i }}</a>
    {% endfor %}

    {% if arts.has_next %}
        <a href="{% url 'user:articles'%}?page={{arts.next_page_number}}">下一页</a>
    {% endif %}
</p>



{% endblock %}
```
3.django自带的分页的库 Paginator  
导入库
```
from django.core.paginator import Paginator
```
>Paginator基本语法  
>Pagintator:对象创建:Paginator(数据集,每一页数据)  
>page:具体的某一页  
>方法:page(页码):获取的一个page对象,页码不存在则抛出invalidPage的异常

>page对象  
>方法:  
>has_next() :判断是否有下一页  
>has_previous():判断是否有上一页  
>has_other_pages():判断是否有上一页或下一页  
>next_page_number():返回下一页的页码  
>pervious_page_number():返回上一页的页码  
>len():返回当前页的数据的个数

### 4.日志
1.在项目文件夹下创建一个logs文件夹,用来存储日志文件

2.在settings.py文件下配置日志
```
# 配置日志
LOGGING = {
    # 必须是1
    'version': 1,
    # 默认为True，禁用日志
    'disable_existing_loggers': False,
    # 定义formatters组件，定义存储日志中的格式
    'formatters':{
        'default': {
            'format': '%(levelno)s %(name)s %(asctime)s'
        }
    },
    # 定义loggers组件，用于接收日志信息
    # 并且将日志信息丢给handlers去处理
    'loggers':{
        '':{
            'handlers': ['console'],
            'level': 'INFO'
        }
    },
    # 定义handlers组件，用户写入日志信息
    'handlers':{
        'console':{
            'level': 'INFO',
            # 定义存储日志的文件
            'filename': '%s/log.txt' % os.path.join(BASE_DIR,'logs'),
            # 指定写入日志中信息的格式
            'formatter': 'default',
            # 指定日志文件超过5M就自动做备份
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
        }
    }
}

```
3.写中间件
```
class LoggingMiddleware(MiddlewareMixin):

    def process_request(self,request):

        # 记录当前请求访问服务器的时间,请求参数,请求内容..
        request.init_time = time.time()
        request.init_body = request.body
        return None

    def process_response(self,request,response):
        try:
            # 记录返回响应的时间和访问服务器的时间的差,记录返回状态码..
            times = time.time() - request.init_time
            # 响应状态码
            code = response.status_code
            # 响应内容
            res_body = response.content
            # 请求内容
            req_body = request.init_body

            # 日志信息
            msg = '%s %s %s %s'%(times,code,res_body,req_body)
            # 写入日志
            logging.info(msg)
        except Exception as e:
            logging.critical('log error,Exception: %s' % e)

        return response
```
4.logging的组成
>Loggers:Loggers为日志系统的入口.每个loggers是一个具名的容器,可以向它写入需要处理的消息  
>Handlers:Handler决定如何处理logger中的每条消息.他表示一个特定的日志行为.与logger一样,handler也有一个日志级别.如果消息的日志级别小于handler的级别,handler将忽略该消息.Logger可以有多个handler,而每个handler可以有不同的日志级别  
>Filter:Filter用于从logger传递给handler的日志记录额外的控制  
>Formatters:日志记录需要转换成文本.Formatter表示文本的格式.Fomatter通常由包含日志记录属性的python格式字符串组成.
