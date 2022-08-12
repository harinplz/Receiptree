from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .models import User
from .models import User_info

def mypage(request):

    return render(request, 'mypage_05.html')


def signup_done(request):
    return render(request, 'signup_11.html')


# 회원가입 (유효성 검사x)
def signup(request):
    if request.method == 'POST':
        # 이름, 비밀번호, 이메일
        if request.POST['password1'] == request.POST['password2']:
            user = User()
            user.username = request.POST['email']
            user.email = request.POST['email']
            user.password = request.POST['password1']
            user.nickname = request.POST['nickname']
            user.phone_number = request.POST['phone']
            user.notify_cnt = 0
            user.grade = "BLUE"
            user.save()
            user_info = User_info()
            # user_info.user_no = user.user_no
                # image = request.FILES.get['image'],
            if request.POST['age']!="나이 입력(숫자만)":
                user_info.age = request.POST['age']
                user_info.job = request.POST['job']
                user_info.income = request.POST['income']
                user_info.expense = request.POST['expense']
                user_info.expense_body = request.POST['expense_body']
                user_info.save()
            # auth.login(request, user)
            # render(request, 'signup_11.html')
            # if request.method == 'POST':
            #     return render(request, 'login_14.html')
            return redirect('login') #회원가입, 로그인 후 이동할 곳
        return render(request, 'signup_09.html')
    return render(request, 'signup_09.html')


# 로그인
def login(request):
    if request.method == 'POST':
        name = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(request, username=name, password=pwd )
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_14.html', {'error': 'YOUR Email or Password is incorrect.'})
    else:
        return render(request, 'login_14.html')
        

# 로그아웃
@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')


# 회원탈퇴
def signout(request):
    if request.method == 'POST':
        pwd = request.POST['password']
        user = request.user
        if check_password(pwd, user.password):
            user.delete()
            return redirect('home')
    return render(request, 'signout.html')



# 비밀번호 변경
def pwd_change(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("mypage")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "pwd_change.html",context)

