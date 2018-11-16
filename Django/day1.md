## day1 Django

#### MVC
MVC模式:模型-视图-控制器    
&emsp;&emsp; M(模型层):数据存取层.用于封装应用程序的业务相关的数据.以及对数据的处理  
&emsp;&emsp;V(视图层):即表现层.负责数据的显示和呈现.渲染的HTML页面给用户,或者返回数据给用户  
&emsp;&emsp;C(业务层):即业务逻辑层.负责从用户端收集用户的输入,进项业务逻辑处理,包括向模型中发送数据,进行CRUD操作  

#### MVT
Django ===> MVT  
MVT模式:  
Model(模型层):负责业务和数据库的对象  
View(视图):负责业务逻辑并适当调用Model和Template  
Template(模板):负责把页面渲染展示给用户,html  

#### 创建环境
virtualenv  
创建虚拟环境  
1.创建一个env的文件夹,专门用来存放虚拟环境  
2.进入env文件夹    
a.virtualenv --no-site-packages <文件夹>     (纯净的虚拟环境)  

b.virtualenv --no-site-packages  -p <python版本路径> <文件夹>   (针对同时安装多个版本python)  
3.pip list (查看虚拟环境下安装的所有的包)  
4.pip freeze(查看虚拟环境中通过pip安装的包)  
5.进入env文件夹里面的新建的文件夹里面,再进入Scripts文件夹里  , 运行activate 命令进入虚拟环境  
6.在这个虚拟环境里面就可以安装你想安装的东西  
7.deactivate 退出虚拟环境

#### 创建项目
>django-admin startproject 项目名day1  
&emsp;&emsp;day1工程目录文件夹,__init__.py,settings.py,wsgi.py,urls.py  
&emsp;&emsp;manage.py:工具集管理入口

##### 启动
>IP:0.0.0.0 PORT:80  
>python manage.py runserver IP:PORT
>python manage.py runserver PORT

##### 访问管理后台 admin
> http://127.0.0.1:8080/admin/

##### 修改数据库配置settings.py

>ENGINE,USER,PASSWORD,HOST,PORT,NAME

##### 映射模型到数据库中
>pythonmanage.py migrate

##### 安装数据库驱动
>pip install pymysql

##### 初始化数据库的驱动__init__.py
>import pymysql
>pymysql.install_as_mysqldb()

##### 创建超级管理员命令

>python manage.py createsuperuser