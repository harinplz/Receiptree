from django.shortcuts import render

def mypage(request):
    return render(request, 'mypage_05.html')

def signup(request):
    return render(request, 'signup_09.html')
