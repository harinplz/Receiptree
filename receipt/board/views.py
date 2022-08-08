from django.shortcuts import redirect, render
from .models import Board, Tag

# Create your views here.

#영수증 메인 화면
def board(request):

    board_list = Board.objects.all()
    keyword = request.POST.get('search_button')
    tag = Tag.objects.filter(tagname = keyword)
    post = Board.objects.filter(tags__in = tag).order_by('-date')

    return render(request, 'receipt_01.html', {'board':board_list, 'post':post, 'keyword':keyword})





def write(request):
    return render(request, 'write_02.html')
