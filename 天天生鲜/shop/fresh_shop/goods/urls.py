
from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    # ��Ʒ����
    url(r'^detail/(\d+)/',views.detail,name='detail'),
]

