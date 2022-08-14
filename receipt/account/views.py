from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import User

def mypage(request):
    user = request.user
    if user.is_authenticated:
        if user.notify_cnt <= 10:
            user.grade = "BLUE"
            user.save()
        elif user.notify_cnt <= 20:
            user.grade = "GREEN"
            user.save()
        elif user.notify_cnt <= 30:
            user.grade = "YELLOW"
            user.save()
        elif user.notify_cnt <= 40:
            user.grade = "ORANGE"
            user.save()
        elif user.notify_cnt <= 50:
            user.grade = "RED"
            user.save()
        else:
            user.grade = "BLACK"
            user.save()
    return render(request, 'mypage_05.html')

def mypage_change(request):
    user = request.user
    if request.method == 'POST':
        # 수정하면 바뀌도록 (수정을 안 하면...?)
        user.phone_number = request.POST['phone']
        user.age = request.POST['age']
        user.job = request.POST['job']
        user.income = request.POST['income']
        user.expense = request.POST['expense']
        user.save()
        return redirect('mypage')
    return render(request, 'mypage_03.html')

def signup_done(request):
    return render(request, 'signup_11.html')

def view_receipt(request):
    return render(request, 'mypage_07.html')


# 회원가입 (유효성 검사x)
def signup(request):
    if request.method == 'POST':
        # 이름, 비밀번호, 이메일
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['email'],
                email = request.POST['email'],
                password = request.POST['password1'],
                nickname = request.POST['nickname'],
                phone_number = request.POST['phone'],
                notify_cnt = 0,
                grade = "BLUE",
                written = 0,
                party_num = 0,
            )
            # user.save()
            # user_info = User_info()
            # user_info.user_no = user.user_no
            # user_info.user_no = user.user_no
                # image = request.FILES.get['image'],
            if request.POST['age']!="":
                user.age = request.POST['age']
                user.job = request.POST['job']
                user.income = request.POST['income']
                user.expense = request.POST['expense']
                user.expense_body = request.POST['expense_body']
            user.save()
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
def logout(request):
    auth.logout(request)
    return redirect('home')


# 회원탈퇴
def signout(request):
    user = request.user
    user.delete()
    return redirect('mypage')
    # if request.method == 'POST':
    #     pwd = request.POST['password']
    #     user = request.user
    #     if check_password(pwd, user.password):
            # user.delete()
            # return redirect('home')
    # return render(request, 'signout.html')



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

