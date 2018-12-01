#coding=utf-8
import os
import random

from flask import redirect, url_for, Blueprint, request, render_template, jsonify, session

import re

from app.models import db, User
from utils.functions import is_login
from utils.settings import UPLOAD_DIR

user_blue = Blueprint('user',__name__)

@user_blue.route('/create_db/')
def create_db():
    # 创建数据库
    db.create_all()
    return '创建数据库成功'


@user_blue.route('/get_code/',methods=['GET'])
def get_code():
    # 获取随机长度为四的验证码
    s='1234567890qwertyuiopasdfghjklzxcvbnm'
    code=''
    for i in range(4):
        code += random.choice(s)
    session['code'] = code
    return jsonify(code=200,msg='请求成功',data=code)


@user_blue.route('/register/',methods=['GET'])
def register():

    return render_template('register.html')


#注册
@user_blue.route('/register/',methods=['POST'])
def my_register():
    mobile = request.form.get('mobile')
    code = request.form.get('imagecode')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if not all([mobile,password,password2]):
        return jsonify({'code':1001,'msg':'参数不完整'})

    # 验证手机号是否正确
    if not re.match(r'^1[3456789]\d{9}$',mobile):
        return jsonify({'code':1002,'msg':'手机号不正确'})

    # 验证验证码是否成功
    if code != session.get('code'):
        return jsonify({'code':1005,'msg':'验证码输入错误'})

    # 验证两次密码是否一致
    if password2 != password:
        return jsonify({'code':1003,'msg':'两次密码不一致'})

    if User.query.filter(User.phone==mobile).count():
        return jsonify({'code':1004,'msg':'该手机号已注册'})

    user = User()
    user.phone = mobile
    user.password = password
    user.name = mobile

    try:
        user.add_update()
        return jsonify({'code':200,'msg':'注册成功'})
    except:
        return jsonify({'code':500,'msg':'注册失败'})


@user_blue.route('/login/',methods=['GET'])
def login():
    return render_template('login.html')

# 登录
@user_blue.route('/login/',methods=['POST'])
def my_login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    if not all([mobile,password]):
        return jsonify({'code':1005,'msg':'参数不完整'})
    user = User.query.filter(User.phone==mobile).first()
    if not user:
        return jsonify({'code':1006,'msg':'该用户没有注册'})

    if user.check_pwd(password):
        session['user_id'] = user.id
        return jsonify({'code': 200, 'msg': '登录成功'})
    else:
        return jsonify({'code':1007,'msg':'密码不正确'})


# 个人信息
@user_blue.route('/my/',methods=['GET'])
@is_login
def my():

    return render_template('my.html')

@user_blue.route('/user/', methods=['GET'])
@is_login
def user_info():
    user = User.query.get(session['user_id'])
    return jsonify(code=200, data=user.to_basic_dict())

# 修改个人信息
@user_blue.route('/profile/',methods=['GET'])
@is_login
def profile():
    return render_template('profile.html')


# 修改用户名
@user_blue.route('/profile/',methods=['POST'])
@is_login
def my_profile():
    name = request.form.get('name')
    id = session.get('user_id')
    user = User.query.filter(User.id==id).first()
    name_all = User.query.filter(User.name==name).first()
    if name_all:
        return jsonify({'code':1008,'msg':'此用户名已存在,请重新输入'})

    user.name=name
    try:
        user.add_update()
        return jsonify({'code':200,'msg':'修改用户名成功'})
    except:
        return jsonify({'code':1009,'msg':'修改用户名失败'})

# 上传头像
@user_blue.route('/profile/',methods=['PATCH'])
@is_login
def user_profile():

    file = request.files.get('avatar')

    # 保存
    image_path = os.path.join(UPLOAD_DIR,file.filename)
    file.save(image_path)

    user = User.query.get(session['user_id'])
    avatar_path = os.path.join('upload',file.filename)
    user.avatar = avatar_path

    try:
        user.add_update()
    except Exception as e:
        db.session.rollback()
        return jsonify({'code':1010,'mag':'数据库错误'})

    return jsonify(code=200,image_url=avatar_path)



# 注销
@user_blue.route('/logout/', methods=['GET'])
@is_login
def user_logout():
    session.clear()
    return redirect(url_for('user.login'))


# 实名认证
@user_blue.route('/auth/', methods=['GET'])
def auth():

    return render_template('auth.html')

@user_blue.route('/auth/',methods=['POST'])
@is_login
def my_auth():
    real_name = request.form.get('id_name')
    id_card = request.form.get('id_card')

    if not all([real_name,id_card]):
        return jsonify({'code':1012,'msg':'参数不完整'})

    if not re.match(r'^[1-9]\d{17}$', id_card):
        return jsonify({'code':1011,'msg':'身份证不正确'})

    user = User.query.filter(User.id_card==id_card).first()
    if user:
        return jsonify({'code':1020,'msg':'该身份证已实名认证过'})



    user = User.query.get(session['user_id'])
    user.id_card = id_card
    user.id_name = real_name
    try:
        user.add_update()
        return jsonify({'code':200,'msg':'实名认证成功'})
    except:
        return jsonify({'code':1013,'msg':'实名认证不成功'})


@user_blue.route('/auth_person/', methods=['GET'])
@is_login
def auth_info():
    user = User.query.get(session['user_id'])
    data = user.to_auth_dict()
    if bool(data['id_name']):
        return jsonify(code=200, data=data)
    return jsonify(code=100,data=data)




