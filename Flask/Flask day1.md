## 1.Flask 环境创建
>1.创建虚拟环境
    virtualenv --no-site-packages flaskenv  
    2. 安装flask  
    pip install flask
    
## 2.flask 最小应用
```python
form flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host,port,debug)
```
## 3.默认启动命令 
python hello.py  
默认id和端口:127.0.0.1:5000

## 4.使用flask_script 的Manager模块
```python
from flask import Flask
form flask_script import Manager
app = Flask(__name__)

# 使用Manage管理app对象
manage = Manager(app)

if __name__ == '__main__':
    manage.run()
```
>启动命令:python hello.py runserver -h IP -p PORT -d
## 5.分离出视图层,业务逻辑,从hello.py中分离出路由和视图函数.

**使用蓝图管理路由,蓝图的好处就是模块化管理应用**

 ```
 from flask import Blueprint
 # 第一步,获取蓝图对象
 blue = Blueprint('xxx',__name__)
 
 # 管理路由
 <!--eg-->
 @app_blueprint.route('/students/<int:id>/')
def student(id):
    return '我的学号是%d' % id
 
 
 # 第二步,注册蓝图
 app.register_blueprint(blueprint=blue,url_prefix='xxx')
 ```

## 6.跳转
```
# 要导入相应的包
@app_blueprint.route('/redirect/')
def redirect_url():
    #django写法:HttpResponseRedirect(reverse('namespace:name'))
    #Flask写法:redirect(url_for('蓝图名称.跳转的函数名'))
    return redirect(url_for('app.hello_world'))
```
## 7.请求与响应
#### 1.请求request  
>1.1 args-->GET请求参数包装  
a)args是get请求参数的包装,args是一个ImmutableMultiDict对象，类字典结构对象  
b)数据存储也是key-value  
1.2 form-->POST请求采纳数包装  
a) form是post请求参数的包装,args是一个ImmutableMultiDict对象，类字典结构对象  
b)数据存储也是key-value  
这里的key可以存在多个相同的key

#### 2.响应Response
Response是由开发者自己创建的  
创建方法:
>from flask import make_response  
make_response创建一个响应,是一个真正的Response对象

例子:
```
@app_blueprint.route('/make_response/', methods=['GET'])
def make_my_response():
    res = make_response('<h2>今天好热</h2>')
    return res
```
**methods请求方法**
>GET:获取  
POST:创建  
PUT:修改(全部属性都修改)  
DELETE:修改  
PATCH:修改(修改部分属性)

## 8.异常抛出与捕获
```
@app_blueprint.route('/abort_a/', methods=['POST'])
def abort_a():
    try:
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = a/b
        return '%s/%s=%s' % (a, b, c)
    except Exception as e:
        # 异常抛出
        abort(500)

@app_blueprint.errorhandler(500)
def error_handler(error):
    # TODO:返回错误页面
    return 'Exception is %s' % error
```

## 9.路由规则
>路由选择规则  
<选择器:参数名>  
选择器有 int:表示接受的参数为int类型  
没有定义选择器:表示接收的参数为string类型(默认)  
选择器string:表示接受到的参数一定为string类型  
选择器 uuid(只接受uuid字符串)/path(接受路径,接收到额时候是str,/也当做字符串的一个字符)/float(浮点型)