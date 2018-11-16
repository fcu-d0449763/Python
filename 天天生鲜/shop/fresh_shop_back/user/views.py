from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm
from django.contrib import auth

def login(request):
    if request.method == 'GET':
        #GET请求返回登录页面
        return render(request,'login.html')

    if request.method == 'POST':
        #将请求参数给form表单做验证
        data = request.POST
        form = UserLoginForm(data)
        #校验结果，返回true表示校验成功
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if not user:

                return render(request, 'login.html')

            #实现登录
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:index'))

        else:
            #验证失败

            errors = form.errors
            return render(request,'login.html',{'errors':errors})

@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

