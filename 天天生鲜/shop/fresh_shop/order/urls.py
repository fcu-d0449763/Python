
from django.conf.urls import url

from order import views

urlpatterns = [

    # �µ�
    url(r'^order/',views.order,name='order'),
    # ��������
    url(r'^user_order/',views.user_order,name='user_order'),
    # �ջ���ַ
    url(r'^user_order_site/',views.user_order_site,name='user_order_site'),



]
