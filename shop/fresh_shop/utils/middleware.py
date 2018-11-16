from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import re

from user.models import User
from cart.models import ShoppingCart

class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # TODO:ĳЩҳ����Ҫ��¼���ܷ���,ĳЩ����Ҫ��¼�Ϳ��Է���
        # TODO:��Ҫ��¼��ҳ��,��û���û���¼ʱ,����δ���
        # ��request.user��ֵ,����ֵΪ��ǰ��¼ϵͳ���û�����
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
            # ���Է������е�ҳ��
            return None

        # û�е�¼,��û��user_id
        # ˼·:��ҳ,����ҳ��,��¼,ע��,����media,����static ,���ܵ�¼��񶼿��Բ鿴
        # �µ�,����,����ҳ��,��������ҳ��ֻ�ܵ�¼���ܲ鿴,û�е�¼,��ת����¼ҳ��
        not_need_path = ['/user/login/','/user/register/',
                         '/goods/index/','/goods/detail/(.*)',
                         '/media/(.*)','/static/(.*)','/cart/add_cart/',
                         '/cart/cart/']
        path = request.path
        for not_path in not_need_path:
            # ƥ�䵱ǰ·���Ƿ�Ϊ����Ҫ��֤��¼��·��
            if re.match(not_path,path):
                return None

        # ��ǰ������url����not_need_path��,��ʾ��ǰurl��Ҫ��¼���ܷ���
        return HttpResponseRedirect(reverse('user:login'))


class SessionUpdate(MiddlewareMixin):
    def process_request(self,request):
        # session����Ʒ���ݺ͹��ﳵ���е����ݵ�ͬ������
        # session�����ݽṹ:[[id,num,is_select],[],[]]
        session_goods = request.session.get('goods')
        user_id = request.session.get('user_id')
        if user_id:
            # �û���¼��,����ͬ��
            if session_goods:
                # ˼·:ʱ�̱���session�����ݺ����ݿ�������ͬ��
                # ���session����Ʒ�Ѿ����������ݿ����,�����
                # ���session����Ʒ�����������ݿ����,�����
                # ���session�е���Ʒ�������ݱ��е���Ʒ,�����session

                # ��session������ͬ�������ݿ�
                for goods in session_goods:
                    # goods�ṹ[id,num,is_select]
                    cart = ShoppingCart.objects.filter(user_id=user_id,
                                                goods_id=goods[0]).first()
                    if cart:
                        # ���ݿ����ܲ�ѯ������Ʒ��Ϣ,���޸�
                        cart.nums = goods[1]
                        cart.is_select = goods[2]
                        cart.save()

                    else:
                        # ���ݿ��в�ѯ��������Ʒ��Ϣ,�����
                        ShoppingCart.objects.create(user_id=user_id,
                                                    goods_id=goods[0],
                                                    nums=goods[1],
                                                    is_select=goods[2])

            # �����ݿ�������ͬ����session
            carts = ShoppingCart.objects.filter(user_id=user_id).all()
            # session�����ݽṹ:[[id,num,is_select],[],[]]
            session_new_goods = [[cart.goods_id,cart.nums,cart.is_select] for cart in carts]
            request.session['goods'] = session_new_goods
        return None