## 1.模型定义
	AutoField
	CharField
	IntegerField
	BooleanField
	DateTimeField
	DateField
## 2.约束
	primary_key
	unique
	default
	auto_now:用于记录每一次修改时间
	auto_now_add:用于记录第一次的时间
## 3.定义表名
	
	class Meta:
		db_table = 'student'
	如果指定db_table参数,则在迁移后在数据库中的表名为student
	如果没有指定db_table参数,在数据库中表名为'应用app的名称_模型名

小写'
	
## 4.迁移
	# 生成迁移文件
	python manage.py makemigrations
	# 执行迁移
	python manage.py migrate
## 5.模型的CRUD
- 创建  
1.方法一(常用):模型名.objects.create(name=xxx,age=xxx)  
2.方法二:  
例:

```
    stu = Student()(得到对象)
    stu.s_name = '小王'
    stu.s_age = 22
    stu.save()
```
- 查询    

1.查询所有:
```
模型名.objects.all()  
```
2.查询满足条件:
		
```
模型名.objects.filter(条件1).filter(条件2)
模型名.objects.filter(条件1,条件2)
```
	  
3.查询第一个,最后一个
```
first(),last()
```
4.获取确定的某一个:
```
模型名.objects.get(条件)
注意:条件不满足获取不到数据,则报错
	满足条件的数据多于一个对象,则报错
```
5.排除满足条件的数据:
```
模型名.objects.exclude(条件)
```
6.返回的结果序列化:
```
模型名.objects.values(字段1,字段2...)
```
7.排序:
```
升序:模型名.objects.order_by('id')
降序:模型名.objects.order_by('-id')
```
8.查询过滤条件:字段__contains
```
contains,startswith,endswith,gt,gte,lt,lte
```
- 删除
```
模型名.objects.filter(条件).delete()
```
- 修改
```
方法一:
模型名.objects.filter(条件).update(字段1=xxx,..)
方法二:
模型名.objects.filter(条件)
模型名.s_name = '...'
模型名.save()
```


