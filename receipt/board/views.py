from django.shortcuts import redirect, render

from .models import *
from django.utils import timezone

# Create your views here.

#영수증 메인 화면
def board_main(request):

    board_list = Board.objects.all()
    keyword = request.POST.get('search_button')
    tag = Tag.objects.filter(tagname = keyword)
    post = Board.objects.filter(tags__in = tag).order_by('-date')
    hot_list = Board.objects.all().order_by('-good_cnt')[0:4]

    return render(request, 'receipt_01.html', {'board':board_list, 'post':post, 'keyword':keyword, 'hot':hot_list})



def board_write(request):

    if request.method == 'GET':
        return render(request, 'write_02.html')
    elif request.method == 'POST':
        tags = request.POST['tags'].split(',')

        board = Board()
        board.title = request.POST['title']
        board.date = timezone.datetime.now()
        board.body = request.POST['body']
        board.user_no = request.user
        board.save()

        for tag in tags:
            tag = tag.strip()
            if not tag:
                continue
            _tag, _ = Tag.objects.get_or_create(tagname=tag)
            board.tags.add(_tag)

        return redirect('board_write')
    return render(request, 'write_02.html')
