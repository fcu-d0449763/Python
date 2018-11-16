
from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    # ÉÌÆ·ÏêÇé
    url(r'^detail/(\d+)/',views.detail,name='detail'),
]

