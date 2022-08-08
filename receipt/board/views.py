from django.shortcuts import render
from .models import Board, Tag

# Create your views here.

#영수증 메인 화면
def board(request):

    board_list = Board.objects.all()
    return render(request, 'receipt_01.html', {'board':board_list,})


def write(request):
    return render(request, 'write_02.html')
