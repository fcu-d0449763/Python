#coding=utf-8
from django.shortcuts import render

# Create your views here.
from goods.models import Goods, GoodsCategory




def index(request):
    if request.method == 'GET':
        # 不可取
        # fruits = Goods.objects.filter(category_id = 1).all()
        # seafoods = Goods.objects.filter(category_id=2).all()
        # meats = Goods.objects.filter(category_id=3).all()
        # poultrys = Goods.objects.filter(category_id=4).all()
        # vegetables = Goods.objects.filter(category_id=5).all()
        # freezes = Goods.objects.filter(category_id=6).all()

        # 第三种,可取
        # {
        #   category1:[Goods object1,Goods object2],
        #   category2:[Goods object1,Goods object2],
        #   category3:[Goods object1,Goods object2],
        #   category4:[Goods object1,Goods object2],
        #   category5:[Goods object1,Goods object2],
        #   category6:[Goods object1,Goods object2],
        # }
        categorys = GoodsCategory.CATEGORY_TYPE
        goods = Goods.objects.all()
        goods_dict = {}
        for category in categorys:
            goods_list = []
            count = 0
            for good in goods:
                # 判断商品分类
                if count < 4:
                    if category[0] == good.category_id:
                        goods_list.append(good)
                        count += 1
            # {'新鲜水果':[],'肉':...}
            goods_dict[category[1]] = goods_list
        return render(request,'index.html',{'goods_dict':goods_dict})

def detail(request,id):
    if request.method == 'GET':
        # 查看商品详情,返回商品对象
        goods = Goods.objects.filter(pk=id).first()
        return render(request,'detail.html',{'goods':goods})