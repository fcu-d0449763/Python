
# coding=utf-8
from django import forms

from goods.models import Goods, GoodsCategory


class AddGoods(forms.Form):
    name = forms.CharField(max_length=100,required=True,
                           error_messages={
                               'required':'商品名必填'
                           })
    goods_sn = forms.CharField(max_length=50,required=True,
                               error_messages={
                                   'required':'货号必填'
                               })
    category = forms.CharField(max_length=10,required=True,
                               error_messages={
                                   'required':'分类必填'
                               })
    goods_nums = forms.IntegerField(required=True,
                                    error_messages={
                                        'required':'库存必填'
                                    })
    market_price = forms.FloatField(required=True,
                                    error_messages={
                                        'required':'市场价格必填'
                                    })
    shop_price = forms.FloatField(required=True,
                                    error_messages={
                                        'required':'本店价格必填'
                                    })
    goods_brief = forms.CharField(max_length=500,required=True,
                                  error_messages={
                                      'required':'描述必填'
                                  })
    goods_front_image = forms.ImageField(required=False)

    # def clean(self):
    #     goods_sn =  self.cleaned_data.get('goods_sn')
    #     goods_sn1 = Goods.objects.filter(goods_sn=goods_sn).first()
    #
    #     if goods_sn1:
    #         raise forms.ValidationError({'goods_sn':'已存在该货号'})

    def clean_category(self):
        id = self.cleaned_data.get('category')
        # 获取分类对象
        category = GoodsCategory.objects.filter(pk=id).first()
        return category

