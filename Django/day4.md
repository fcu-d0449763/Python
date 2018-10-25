### 多对多(昨日剩下内容)

ManyToManyField

```
#多对多
class Course(models.Model):
    c_name = models.CharField(max_length=10)
    # 多对多关联字段
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'
```
**注意:当在两个表之前创建多对多关系的时候,会自动生成第三张表,作为中间表**  
多对多关系：
1. 生成表的时候会多生成一张表（实际会有三张表）
2. 生成的表是专门用来维护关系的
3. 生成的表是使用两个外键来维护多对多的关系
4. 两个一对多的关系来实现多对多的实现　　　
5. 删除一个表的数据的话，中间关联表也要删除相关的信息

### 模板(静态代码+挖坑)
#### 1.标签

```
a.标签:{% tag %}
       {% endtag %}
  eg:{% if xxx %}
     {% endif %}
大概有:for,if,ifequal/extends/block,comment
```
#### 2.父模板:最主要的就是挖坑,让子模板在继承父模板的时候能够在坑的位置填上新的内容
```
<!--这是最简单的模板-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {%block title%}
        {%endblock%}

    </title>
    {% block css%}
    {% endblock %}

    {% block js%}
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    {% endblock %}
</head>
<body>
    {%block content%}
    {%endblock%}
</body>
</html>
```
#### 3.子模板:根据父模板的标签,在不同的标签内写入相应的内容.
eg.
```
{% extends 'base_main.html'%}

{% block content %}
    <table>
        <thead>
            <th>序号</th>
            <th>id</th>
            <th>姓名</th>
            <th>年龄</th>
            <th>创建时间</th>
        </thead>
        <tbody>
            {{content_h2 | safe}}
            {%for stu in stus%}
            
                <tr>
                    
                    <td>{{forloop.counter}}</td>
                    <td>{{stu.id}}</td>
                    <td>
                        {# if forloop.counter == 1 #}

                        {% ifequal forloop.counter 1 %}
                            <em style="color:red">{{stu.s_name}}</em>
                        {%else%}
                            {{stu.s_name}}
                        {% endifequal %}

                    </td>
                    <td>{{stu.s_age | add:1}}</td>

                    <td>{{stu.create_time | date:'Y年m月d日 H:m:s'}}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```
#### 4.在子模板继承父模板的时候
```
{% extends '父模板名字'%}
```
#### 5.注释
```
<!--第一种注释-->
{# 第二种注释 #}
{% comment %}
第三种注释
{% endcomment %}

前两种注释都是单行注释,第一种注释可见,可运行,不建议用这个,第二种推荐使用,不可见.
第三种是多行注释.
```
#### 6.引入js/css
>1.在项目文件夹下创建一个名为static的文件夹,这个文件夹专门存放一些静态文件,比如js,css,图片等静态文件.  
>2.当网页需要引入这些静态文件的时候,需要在settings.py文件最底部下加载配置静态文件
```
STATIC_URL = ‘/static/’
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, ‘static’)
]
```
>3.使用静态文件前,要先进行声明
```
{% load static %} 或者 {% load staticfiles %}
```
>4.引用资源的时候  
eg
```
<link href='/static/xxx.css' rel='stylesheet'/>
或
<link href='{% static 'xxx.css' %}' rel='stylesheet'/>

```

#### 7.其他
```
{{ forloop.counter }} 表示当前是第几次循环，从1开始
{{ forloop.counter0 }} 表示当前从第几次循环，从0开始
{{forloop.revcounter}}表示当前是第几次循环，倒着数数，到1停
{{forloop.revcounter0}}表示当前是第几次循环，倒着数数，到0停
{{forloop.first}} 循环第一次打印True
{{forloop.last}} 循环最后一次打印False
```

#### 8.过滤器(常用)
**|** 此为管道符
1. add:{{value | add:2}} value值增加2
2. date :{{ value | date:"Y-m-d H:m:s"}}  格式化事件格式
3. dictsort:如果value的值是一个字典,那么返回值是按照关键字排序的结果
```
使用形式：{{ value | dictsort:"name"}}，例如，
如果value是：
[{'name': 'python'},{'name': 'java'},{'name': 'c++'},]
那么，输出是：
[{'name': 'c++'},{'name': 'java'},{'name': 'python'}, ]
```
4.join:使用指定的字符串连接一个list,作用如同python的str.join(list)

5.last:返回列表/字符串中的最后一个元素.  
6.length:返回value的长度  
7.center:在一个给定宽度的字段中,中心对齐显示value.  
8.lower:将一个字符串转换成小写形式.
9.random:从给定的list中返回一个任意的item  
10.safe:当系统设置autoescaping打开的时候,该过滤器使得输出不进行escape转换.  
11.wordcount:返回字符串中单词的数目

