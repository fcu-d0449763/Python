from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    # ��¼��֤,��ȡ��¼ϵͳ���û�
    url('is_login/', views.is_login, name='is_login'),
    # ������Ϣ����
    url('user_center_order/', views.user_center_order, name='user_center_order'),
    # �ջ���ַ
    url('user_address/', views.address, name='user_address'),

]

