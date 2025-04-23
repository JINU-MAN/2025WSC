from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST['username'] #여기에 동작코드를 작성하세요
        password=request.POST['password'] #여기에 동작코드를 작성하세요
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '아이디또는비밀번호가올바르지않습ㄴ다.')


    return render(request,'accounts/login.html' )

@login_required
def home_view(request):
    return render(request,'accounts/home.html',{'user':request.user})

def logout_view(request):
    logout(request)
    return redirect('/login')
