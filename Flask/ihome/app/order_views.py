#coding=utf-8
from datetime import datetime

from flask import Blueprint, render_template,  session, request, jsonify

from app.models import House, Order

order_blue = Blueprint('order',__name__)

@order_blue.route('/order/',methods=['POST'])
def order():

    house_id = request.form.get('house_id')
    begin_date = datetime.strptime(request.form.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')

    house = House.query.get(house_id)

    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = (end_date - begin_date).days + 1
    order.house_price = house.price
    order.amount = order.days * order.house_price

    order.add_update()

    return jsonify({'code':200,'msg':'创建订单成功'})


@order_blue.route('/orders/',methods=['GET'])
def orders():
    return render_template('orders.html')


#我的订单
@order_blue.route('/my_orders/',methods=['GET'])
def my_orders():
    orders = Order.query.filter(Order.user_id==session['user_id'])
    orders_list = [order.to_dict() for order in orders]
    return jsonify(code=200, orders_list=orders_list)


#客户订单
@order_blue.route('/lorders/',methods=['GET'])
def lorder():
    return render_template('lorders.html')


@order_blue.route('/my_lorders/', methods=['GET'])
def my_lorders():
    user_id = session['user_id']
    houses = House.query.filter(House.user_id==user_id)
    houses_ids = [house.id for house in houses]

    orders = Order.query.filter(Order.house_id.in_(houses_ids))
    orders_list = [order.to_dict() for order in orders]
    return jsonify(code=200, orders_list=orders_list)


@order_blue.route('/order/', methods=['PATCH'])
def order_status():
    order_id = request.form.get('order_id')
    status = request.form.get('status')
    comment = request.form.get('comment')

    order = Order.query.get(order_id)
    order.status = status
    if comment:
        order.comment = comment
    order.add_update()

    return jsonify({'code':200,'msg':'成功'})
