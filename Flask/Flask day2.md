## 1.flask中session的两种存储方式
1.1.使用flask默认的方式存储session,其实就是将session中的数据保存在客户端的cookie中
```
@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':

        # 获取参数
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'jxc' and password == '123':
            # 模拟校验用户名和密码成功,则向session中存储登录成功后的用户id值
            session['user_id'] = 1
            return redirect('/app/index/')
        else:
            return render_template('login.html')
```
1.2在服务端中保存session数据,使用flask-session库,配置使用redis进行数据存储

1.2.1安装
```
pip install flask-session
pip install redis
```
1.2.2配置  在manage.py文件中
```
# 配置session存储数据库
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',
                                          port=6379)
                                          
# 初始化flask对象app
# 第一种
# Session(app)

# 第二种
sess = Session()
sess.init_app(app)                                          
```
## 2.模板
2.1 继承,block块
>{% extends 'xxx.html' %}   继承父模板  
{% block <name> %}  
    ...  
{% endblock %}  

2.2 继承block中已填有的内容
>{{ super() }}

2.3标签  
>{% 标签 %}  if,for,block,url_for

2.4变量
>{{ 变量 }},loop,loop.index,loop.first,loop.last

2.5 宏定义macro  
例
```
{% macro hello(name) %}
    {{ name }}
{% endmacro %}
# 宏定义,可以在模板中定义函数,在其他地方调用
```
宏定义可导入
```
{% from 'xxx' import xxx %}
```


2.6过滤器 upper,lower,safe,length


## 3.静态文件加载
第一种
例:引入css文件
><link herf="/static/CSS/style.css" rel="stylesheet">
第二种
><link href="{{ url_for('static',filename='CSS/style.css')}}" rel="stylesheet">


## 3.模型层
3.1 安装
```
pip install flask-sqlchemy
pip install pymysql
```
3.2 创建模型,新建一个models.py文件
```

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 第一步:声明模型



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=True)
    # gender = db.Column(db.Boolean,default=1)

    __tablename__ = 'day02_user'
```
3.3在数据库中创建表
```

@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建模型成功'

#  删除模型
# @blue.route('/drop_db/')
# def drop_db():
#     db.drop_all()
#     return '删除模型成功'
```

3.4 在manage.py文件中数据库配置
```
# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRANK_MODIFICATIONS'] =  False


# 初始化app和db
db.init_app(app)
```