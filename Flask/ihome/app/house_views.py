#coding=utf-8
import os

from flask import Blueprint, render_template,  session, request, jsonify

from app.models import Area, Facility, House, db, HouseImage, User, Order

from utils.functions import is_login
from utils.settings import UPLOAD_DIR

house_blue = Blueprint('house', __name__)


@house_blue.route('/myhouse/',methods=['GET'])
@is_login
def myhouse():
    return render_template('myhouse.html')


@house_blue.route('/myhouses/', methods=['GET'])
@is_login
def user_my_house():
    houses = House.query.filter(House.user_id == session['user_id']).all()
    houses_info = [house.to_dict() for house in houses]
    return jsonify(code=200, houses=houses_info)


@house_blue.route('/newhouse/',methods=['GET'])
@is_login
def newhouse():
    return render_template('newhouse.html')


@house_blue.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_list = [area.to_dict() for area in areas]
    facilitys_list = [facility.to_dict() for facility in facilitys]
    return jsonify(code=200,areas=areas_list,facilitys=facilitys_list)


@house_blue.route('/newhouse/',methods=['POST'])
@is_login
def my_newhouse():
    data = request.form.to_dict()
    facility_ids = request.form.getlist('facility')

    house = House()
    house.user_id = session['user_id']
    house.title = data.get('title')
    house.price = data.get('price')
    house.area_id = data.get('area_id')
    house.address = data.get('address')
    house.room_count = data.get('room_count')
    house.acreage = data.get('acreage')
    house.unit = data.get('unit')
    house.capacity = data.get('capacity')
    house.beds = data.get('beds')
    house.deposit = data.get('deposit')
    house.min_days = data.get('min_days')
    house.max_days = data.get('max_days')

    facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
    house.facilities = facility_list
    try:
        house.add_update()
    except:
        db.session.rollback()
    return jsonify(code=200, house_id=house.id)


@house_blue.route('/house_images/',methods=['POST'])
def house_images():
    house_id = request.form.get('house_id')
    house_image = request.files.get('house_image')

    image_path = os.path.join(UPLOAD_DIR,house_image.filename)
    house_image.save(image_path)

    # 图片路径
    image_url = os.path.join('upload',house_image.filename)

    # 保存房屋的首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()


    h_image = HouseImage()
    h_image.house_id = house_id
    h_image.url = image_url
    try:
        h_image.add_update()
    except:
        db.session.rollback()
        return jsonify({'code':0,'msg':'数据库错误'})
    return jsonify(code=200, image_url=image_url)


@house_blue.route('/detail/',methods=['GET'])
def detail():
    return render_template('detail.html')


# 房屋详情接口
@house_blue.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)
    house_info = house.to_full_dict()

    return jsonify(code=200,house_info=house_info)


@house_blue.route('/booking/',methods=['GET'])
def booking():

    return render_template('booking.html')


@house_blue.route('/index/',methods=['GET'])
def index():
    return render_template('index.html')


@house_blue.route('/my_index/',methods=['GET'])
def my_index():
    # 判断用户是否登录
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        username = user.name
    else:
        username = ''

    houses = House.query.filter(House.index_image_url != '')[:3]
    house_image = [house.to_dict() for house in houses ]
    return jsonify(code=200,username=username,house_image=house_image)


@house_blue.route('/search/')
def search():
    return render_template('search.html')


@house_blue.route('/my_search/', methods=['GET'])
def search_house():

    aid = request.args.get('aid')
    sd = request.args.get('sd')
    ed = request.args.get('ed')
    sk = request.args.get('sk')

    house = House.query.filter(House.area_id==aid)


    if 'user_id' in session:
        h_list = house.filter(House.user_id != session['user_id'])



    order1 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= ed)
    order2 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= sd)
    order3 = Order.query.filter(Order.begin_date >= sd, Order.begin_date <= ed)
    order4 = Order.query.filter(Order.begin_date >= sd, Order.end_date <= ed)


    house_ids1 = [order.house_id for order in order1]
    house_ids2 = [order.house_id for order in order2]
    house_ids3 = [order.house_id for order in order3]
    house_ids4 = [order.house_id for order in order4]

    house_ids = list(set(house_ids1 + house_ids2 + house_ids3 + house_ids4))

    houses = h_list.filter(House.id.notin_(house_ids))

    if sk == 'booking':
        houses = houses.order_by('order_count')
    elif sk == 'price-inc':
        houses = houses.order_by('price')
    elif sk == 'price-des':
        houses = houses.order_by('-price')
    else:
        houses = houses.order_by('-id')

    houses_dict = [house.to_dict() for house in houses]

    return jsonify(code=200, house_dict=houses_dict)