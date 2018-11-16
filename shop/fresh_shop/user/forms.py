# coding=utf-8

from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=20,required=True,
                                error_messages={
                                    'required':'用户名必填',
                                    'max_length':'不能超过20个字符'
                                })
    pwd = forms.CharField(max_length=255,required=True,
                          error_messages={
                              'required': '密码必填',
                              'max_length': '不能超过255个字符'
                          })
    cpwd = forms.CharField(max_length=255,required=True,
                          error_messages={
                              'required': '确认密码必填',
                              'max_length': '不能超过255个字符'
                          })
    email = forms.EmailField(max_length=100,required=True,
                            error_messages={
                                'required': '邮箱必填',
                                'max_length': '不能超过100个字符'
                            })

    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        user = User.objects.filter(username=user_name)
        if user:
            raise forms.ValidationError({'user_name': '该账户已注册'})
        if self.cleaned_data.get('pwd') != self.cleaned_data.get('cpwd'):
            raise forms.ValidationError({'pwd': '密码不一致'})

        return self.cleaned_data


class UserAddressForm(forms.Form):
    # 用户地址保存的表单验证
    signer_name = forms.CharField(required=True, error_messages={'required': '收件人必填'})
    address = forms.CharField(required=True, error_messages={'required': '详细地址必填'})
    signer_mobile = forms.CharField(required=True, error_messages={'required': '收件人手机号码必填'})
    signer_postcode = forms.CharField(required=True, error_messages={'required': '邮编必填'})
