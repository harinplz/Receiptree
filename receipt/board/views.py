from django.shortcuts import render
from .models import Board

# Create your views here.

#영수증 메인 화면
def board(request):
    return render(request, 'receipt_01.html')


def write(request):
    return render(request, 'write_02.html')
