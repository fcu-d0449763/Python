## 1.数据库的增删改查
1.1 在models.py文件中创建表
```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name = db.Column(db.String(10),unique=True,nullable=False)
    gender = db.Column(db.Boolean,default=1)
    
    # __tablename__ 用于指定模型映射的表名,如果没有指定,则表名为模型名的小写
    
    def save(self):
    db.session.add(self)
    db.session.commit()
```
**1.2 在views.py中**  
1.2.1 创建数据库
```
@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建数据库成功'
```

1.2.2 插入数据
```
@blue.route('/add_stu/',methods=['POST'])
def add_stu():
    # 插入数据
    stu = Student()
    stu.s_name = '小张'
    # db.session.add(stu)
    # db.session.commit()
    stu.save()
    return '添加学生成功'
```
1.2.3 删除学生
```
@blue.route('/del_stu/',methods=['DELETE'])
def del_stu():
    # 删除数据
    stu = Student.query.filter(Student.s_name == '小张').first()
    db.session.delete(stu)
    db.session.commit()
    return '删除学生成功'
```
1.2.4 更新学生
```
@blue.route('/up_stu/',methods=['PATCH'])
def up_stu():
    # 第一种
    # stu = Student.query.filter(Student.s_name == '小江').first()
    # stu.s_name = '西瓜'
    # stu.save()
    # 第二种
    Student.query.filter(Student.s_name == '西瓜').update({'s_name':'小江'})
    db.session.commit()
    
    return '更新学生成功'
```
1.2.5 查询学生
```
@blue.route('/sel_stu/',methods=['GET'])
def sel_stu()
    # filter(模型.字段 == '值')
    # filter(字段 = '值')
    stu = Student.query.filter_by(s_name='小江').first()
    # all():查询所有结果,返回结果的列表
    # first():返回对象
    # 注意:不要写all().first()
    
    # 查询id为1的学生,使用get()方法
    # get():获取主键所在行的对象,如果获取不到,返回空
    stu = Student.query.get(1)
    
    # order_by():排序
    # 降序:-id,id desc
    # 升序:id,id asc
    stu = Student.query.order_by('-id')
    
    # 使用运算符
    # Django:filter(s_name__contains='111')
    # Flask中SQLALchemy中:filter(模型名.s_name.contains(''))
        # 例子:模糊查询姓名中包含'张'的学生信息
    stus = Student.query.filter(Student.s_name.contains('张')).all()
    # startswith,endswith,like,contains
    stus = Student.query.filter(Student.s_name.startswith('小')).all()
    stus = Student.query.filter(Student.s_name.endswith('张')).all()
    # 查询姓名中包含'李'的学生信息,使用like,%,_
    stus = Student.query.filter(Student.s_name.like('%张%')).all()

    # in_()查询某个范围之内的对象
    stus = Student.query.filter(Student.id.in_([1,2,3,4,5])).all()


    # 查询id大于5的学生信息,
    # 大于 __gt__  大于等于 __ge__
    # 小于 __lt__  小于等于 __le__
    stus = Student.query.filter(Student.id.__gt__(5)).all()
    stus = Student.query.filter(Student.id > 5).all()

    # 分页
    page = request.args.get('page',1)
    paginate = Student.query.paginate(int(page),2)
    stus = paginate.items
    # return render_template('stus.html',stus=stus,paginate=paginate)

    # 例子,查询性别为男的,且姓名中包含'小'的学生信息
    stus = Student.query.filter(Student.gender == 0,Student.s_name.contains('小')).all()

    # and_且,not_非,or_或
    stus = Student.query.filter(and_(Student.gender == 0,
                                     Student.s_name.contains('小'))
                                ).all()
    # 例子,查询性别为男的,或名中包含'小'的学生信息
    stus = Student.query.filter(or_(Student.gender == 1,
                                    Student.s_name.contains('小'))
                                ).all()

    # 例子:查询性别不为男,且名中包含'小'的学生信息
    stus = Student.query.filter(not_(Student.gender == 1),Student.s_name.contains('小')).all()

    stus_names = [stu.s_name for stu in stus]
    return str(stus_names)
    


```

## 2.一对多
2.1 创建一个年级表,和学生表进行连接
```python
#学生表
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name = db.Column(db.String(10),unique=True,nullable=False)
    gender = db.Column(db.Boolean,default=1)
    grade = db.Column(db.Integer,db.ForeignKey('grade.id'),nullable=True)

#年级表
class Grade(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    g_name = db.Column(db.String(10),unique=True,nullable=False)
    student = db.relationship('Student',backref='g')
```
**注意:foreign_key外键定义在多的一方 relationship 关联关系定义在1的一方**




