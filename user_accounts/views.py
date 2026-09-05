from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #注册新用户
    if request.method != "POST":
        #显示空的注册表单
        form =UserCreationForm()
    else:
        #处理编写好的表单
        form = UserCreationForm(data=request.POST)
#GET = 我要东西（伸手拿）索要的内容暴漏在url中，不安全
# POST = 我给你东西（递过去），递交的内容包裹在body中，相对安全。
# 地址栏输入和点击链接，都是“伸手拿”（GET）。
# 只有提交表单，才可能是“递过去”（POST）。

        if form.is_valid():
            new_user=form.save()
            #让用户自动登录，再重新定向到主页

            login(request,new_user)
            return redirect('learning_logs:index')

    #显示空表单或指出表单无效：
    context={'form':form}
    return render(request,'registration/register.html',context)
    

# Create your views here.
