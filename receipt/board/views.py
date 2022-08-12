from django.shortcuts import redirect, render, get_object_or_404

from .models import *
from django.utils import timezone

import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.db.models import Count

# Create your views here.

#영수증 메인 화면
def board_main(request):

    board_list = Board.objects.all()
    keyword = request.POST.get('search_button')
    tag = Tag.objects.filter(tagname = keyword)
    post = Board.objects.filter(tags__in = tag).order_by('-date')
    hot_list = Board.objects.annotate(num_good=Count('good_user')).order_by('-num_good')[:4]
    return render(request, 'receipt_01.html', {'board':board_list, 'post':post, 'keyword':keyword, 'hot':hot_list})


#영수증 작성 화면
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

        if board.title and board.date and board.body is not None:
            board.save()

            for tag in tags:
                tag = tag.strip()
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(tagname=tag)
                board.tags.add(_tag)

        
        dates = request.POST['date[]'].split(',')
        dates = list(dates)
        costs = request.POST['cost[]'].split(',')
        costs = list(costs)
        places = request.POST['place[]'].split(',')
        places = list(places)
        contents = request.POST['content[]'].split(',')
        contents = list(contents)

        if dates and costs and places and contents is not None:

            for i in range(0, len(dates)):
                receipt = Receipt()
                receipt.user_no = request.user
                receipt.board_no = board

                receipt.use_date = dates[i]
                receipt.cost = costs[i]
                receipt.place = places[i]
                receipt.body = contents[i]

                receipt.save()

        return redirect('board_main')
    return redirect('board_main')


#영수증 상세화면
def board_detail(request, board_id):

    # if request.method == 'GET':
        board_detail = get_object_or_404(Board, pk=board_id)
        #board_list = Board.objects.all()
        receipt_list = Receipt.objects.filter(board_no = board_id)
        comment_list = Comment.objects.filter(board_no = board_id)
        # 총 합 계산
        sum = 0
        for receipt in receipt_list:
            sum += receipt.cost


        return render(request, 'writeDetail_02-1.html', 
        {'board_detail': board_detail, 'receipt':receipt_list, 'sum':sum, 'comment_list' : comment_list, })
        
    
#댓글
@login_required
def new_comment(request, board_id):
    newcomment = Comment()

    newcomment.board_no = get_object_or_404(Board, pk=board_id)
    newcomment.user_no = request.user
    newcomment.date = timezone.datetime.now()
    newcomment.body = request.POST['newcomment_body'] #오류 날 가능성 많음

    if newcomment.body != "":
        newcomment.save() #저장

    return redirect('board_detail', board_id)


# '좋은 소비예요' 버튼 기능 구현
@login_required
@require_POST
def board_good(request):
    pk = request.POST.get('pk', None)
    board = get_object_or_404(Board, pk=pk)
    user = request.user


    if board.good_user.filter(user_no=user.user_no): #오류나면 여기 확인
        board.good_user.remove(user)
    else:
        board.good_user.add(user)

    context = {'good_count':board.count_good_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")


# '나쁜 소비예요' 버튼 기능 구현
@login_required
@require_POST
def board_bad(request):
    pk = request.POST.get('pk', None)
    board = get_object_or_404(Board, pk=pk)
    user = request.user

    if board.bad_user.filter(user_no=user.user_no):
        board.bad_user.remove(user)
    else:
        board.bad_user.add(user)
    
    context={'bad_count': board.count_bad_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")



