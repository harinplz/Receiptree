from django.shortcuts import redirect, render, get_object_or_404

from .models import *
from django.utils import timezone

import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

#영수증 메인 화면
def board_main(request):

    board_list = Board.objects.all()
    keyword = request.POST.get('search_button')
    tag = Tag.objects.filter(tagname = keyword)
    post = Board.objects.filter(tags__in = tag).order_by('-date')
    hot_list = Board.objects.all()[0:4]
    #hot_list = Board.objects.all().order_by('-good_cnt')[0:4]

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


        
        #receipt.use_date = request.POST['date[]']
        # receipt.cost = request.POST['cost']
        # receipt.place = request.POST['place']
        # receipt.body = request.POST['content']

        #receipt.save()

        return redirect('board_write')
    return render(request, 'write_02.html')


#영수증 상세화면
def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    #board_list = Board.objects.all()
    receipt_list = Receipt.objects.filter(board_no = board_id)
    
    # 총 합 계산
    sum = 0
    for receipt in receipt_list:
        sum += receipt.cost

    # 댓글
    comment_list = Comment.objects.filter(board_no = board_id)
    #print(sum)
    #print(receipt_list)
    return render(request, 'writeDetail_02-1.html', 
    {'board': board, 'receipt':receipt_list, 'sum':sum, 'comments' : comment_list, })


# 좋은 소비예요, 나쁜 소비예요 구현
# @login_required #로그인 한 사용자만이 접근 가능
# @require_POST #POST request만 받기로 함
# def board_good(request):
#     pk = request.POST.get('pk', None)
#     board = get_object_or_404(Board, pk=pk)
#     board_good, board_good_created = board.good_user.get_or_create(user=request.user)

#     if not board_good_created:
#         board_good.delete()
#         message = "좋은 소비예요 취소"
#     else:
#         message = "좋은 소비예요"

#     context = {'good_count' : board.count_good_user,
#                 'message' : message }

#     return HttpResponse(json.dumps(context), context_type="application/json")    
    #user = request.user

    # if board.good_user.filter(id=user.id).exists(): #오류나면 id->user_no 로 변경
    #     board.good_user.remove(user)
    #     message = "'좋은 소비예요' 버튼을 취소하셨습니다."
    # else:
    #     board.good_user.add(user)
    #     message = "'좋은 소비예요' 버튼을 누르셨습니다."

    # context = {'good_count':board.count_good_user(), 'message':message}
    # return HttpResponse(json.dumps(context), content_type="application/json")

