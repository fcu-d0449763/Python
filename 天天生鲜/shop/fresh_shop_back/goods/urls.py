# @Author   :xaidc
# @Time     :2018/11/5 14:44
# @File     :urls.py
from django.conf.urls import url

from goods import views

urlpatterns = [
    # ��Ʒ����
    url(r'^goods_category_list/',views.goods_category_list,name='goods_category_list'),
    # ��Ʒ����༭
    url(r'^goods_category_detail/(\d+)/',views.goods_category_detail,name='goods_category_detail'),
    # ��Ʒ�б�
    url(r'^goods_list/',views.goods_list,name='goods_list'),
    # ��Ʒ���
    url(r'^goods_add/',views.goods_add,name='goods_add'),
    # ɾ����Ʒ
    url(r'^goods_del/(\d+)/',views.goods_del,name='goods_del'),
    # �༭��Ʒ
    url(r'^goods_edit/(\d+)/',views.goods_edit,name='goods_edit'),
    # ��Ʒ����
    url(r'^goods_desc/(\d+)/',views.goods_desc,name='goods_desc'),

]