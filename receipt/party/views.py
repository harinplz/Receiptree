
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect

from .models import *

import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

# 파티 메인화면
def party_main(request):

    #GET으로 받아오기
    team_list = Team.objects.all() #팀 클래스 받아오기
    return render(request, 'party_06.html', {'team':team_list, })


# 파티 메인화면 _ 절약
def party_main_fru(request):

    #GET으로 카테고리가 '절약'인 클래스만 받아오기
    team_fru_list = Team.objects.filter(category = '절약')
    return render(request, 'party_06_frugality.html', {'team': team_fru_list, })


# 파티 메인화면 _  저축
def party_main_saving(request):

    # GET으로 카테고리가 '저축'인 클래스만 받아오기
    team_saving_list = Team.objects.filter(category = '저축')
    return render(request, 'party_06_saving.html', {'team':team_saving_list, })


# 파티 상세화면
def party_detail(request, team_id):
    party_detail = get_object_or_404(Team, pk=team_id)
    party_receipt = Team_Receipt.objects.filter(team_no = team_id)
    party_board = Team_Board.objects.filter(team_no = team_id)
    party_users = [0 for i in range(3)]

    for i, users in enumerate(party_detail.team_users.all()):
        party_users[i] = users 

    # 파티장이 존재할 때
    if party_detail.leader_no != None:
        party_board1 = Team_Board.objects.filter(team_writer_no = party_detail.leader_no, team_no = team_id)
        party_receipt1 = Team_Receipt.objects.filter(team_user_no = party_detail.leader_no, team_no = team_id)
        sum1 = 0
        for cost in party_receipt1.values('team_cost'):
            sum1+=cost.get('team_cost')

    #print(party_users)

    #파티원1이 존재할 때
    if party_users[0] != 0 :
        party_board2 = Team_Board.objects.filter(team_writer_no = party_users[0].user_no, team_no = team_id)
        party_receipt2 = Team_Receipt.objects.filter(team_user_no = party_users[0].user_no, team_no = team_id)
        sum2 = 0
        for cost in party_receipt2.values('team_cost'):
            sum2 += cost.get('team_cost')
    else:
        party_board2 = None
        party_receipt2 = None
        sum2 = None
    
    # 파티원2가 존재할 때
    if party_users[1] != 0:
        party_board3 = Team_Board.objects.filter(team_writer_no = party_users[1].user_no, team_no = team_id)
        party_receipt3 = Team_Receipt.objects.filter(team_user_no = party_users[1].user_no, team_no = team_id)
        sum3 = 0
        for cost in party_receipt3.values('team_cost'):
            sum3 += cost.get('team_cost')
    else:
        party_board3 = None
        party_receipt3 = None
        sum3 = None
    

    # 파티원3이 존재할 때
    if party_users[2] != 0:
        party_board4 = Team_Board.objects.filter(team_writer_no = party_users[2].user_no, team_no = team_id)
        party_receipt4 = Team_Receipt.objects.filter(team_user_no = party_users[2].user_no, team_no = team_id)
        sum4 = 0
        for cost in party_receipt4.values('team_cost'):
            sum4 += cost.get('team_cost')
    else:
        party_board4 = None
        party_receipt4 = None
        sum4 = None
    
    #print(party_detail.count_team_users()-1)

    #댓글
    party_comment = Team_Comment.objects.filter(team_no = team_id)

    context = {'party_detail':party_detail,'party_receipt':party_receipt, 'party_board':party_board, 'party_comment':party_comment,
    'party_receipt1' : party_receipt1, 'party_board1' : party_board1, 'sum1':sum1,
    'party_board2':party_board2, 'party_receipt2':party_receipt2, 'sum2':sum2,
    'party_board3':party_board3, 'party_receipt3':party_receipt3, 'sum3':sum3,
    'party_board4':party_board4, 'party_receipt4':party_receipt4, 'sum4':sum4,
    }
    



    return render(request, 'partyDetail_10.html', context)


# 파티 댓글
@login_required
def newcomment_party(request, team_id):
    newcomment_party = Team_Comment()

    newcomment_party.team_no = get_object_or_404(Team, pk=team_id)
    newcomment_party.team_user_no = request.user
    newcomment_party.team_body = request.POST['newcomment_team_body']
    newcomment_party.team_date = timezone.datetime.now()
    

    newcomment_party.save()

    if newcomment_party.team_body != "":
        newcomment_party.save() #댓글 저장 
        print("실행??")

    return redirect('party_detail', team_id)


# # '좋은 소비예요' 버튼 기능 구현
# @login_required
# @require_POST
# def party_good(request):
#     pk = request.POST.get('pk', None)
#     party_board = get_object_or_404(Team_Board, pk=pk)
#     print(party_board)
#     user = request.user

#     if party_board.team_good_users.filter(user_no = user.user_no):
#         party_board.team_good_users.remove(user)
#     else:
#         party_board.team_good_users.add(user)

#     context = {'party_good_count': party_board.count_team_good_users()}
#     return HTTPResponse(json.dumps(context), content_type="application/json")

# 파티 만들기 화면
def party_make(request):
    if request.method == 'POST':
        if request.POST['team_name']!="":
            team = Team()
            team.team_name = request.POST['team_name']
            team.team_date = timezone.datetime.now()
            team.content = request.POST['content']
            user = request.user
            team.leader_no = user
            team.category = request.POST['category']
            team.save()
            return redirect('party_main')
        return redirect(request, 'party_08.html')
    return render(request, 'party_08.html')

# 파티 가입 화면
def party_getin(request, team_id):
    party_detail = get_object_or_404(Team, pk=team_id)
    # party_users = [0 for i in range(3)]

    # for i, users in enumerate(party_detail.team_users.all()):
    #     party_users[i] = users 
    
    if request.method == "POST":
        user = request.user
        party_detail.team_users.add(user)
        return redirect('party_main')
    
    return render(request, 'party_12.html', {'party_detail':party_detail})


# 파티 영수증 작성화면
def party_write(request, team_id):
    if request.method == 'GET':
        party = get_object_or_404(Team, pk=team_id)
        # print(party)

        return render(request, 'party_write.html', {'party':party} )
    elif request.method == 'POST':
        party_board = Team_Board()

        party_board.team_date = timezone.datetime.now()
        party_board.team_body = request.POST['body']
        party_board.team_no = get_object_or_404(Team, pk=team_id)
        party_board.team_writer_no = request.user

        if party_board.team_date and party_board.team_body and party_board.team_no and party_board.team_writer_no is not None:
            party_board.save()
        
        
        # 영수증 작성
        dates = request.POST['date[]'].split(',')
        dates = list(dates)
        print(dates)
        costs = request.POST['cost[]'].split(',')
        costs = list(costs)
        print(costs)
        places = request.POST['place[]'].split(',')
        places = list(places)
        print(places)
        contents = request.POST['content[]'].split(',')
        contents = list(contents)
        print(contents)

        if dates and costs and places and contents is not None:
            for i in range(0, len(dates)):
                print("실행"+str(i))
                receipt = Team_Receipt()
                receipt.team_no = get_object_or_404(Team, pk=team_id)
                receipt.team_board_no = party_board
                receipt.team_user_no = request.user

                receipt.team_use_date = dates[i]
                receipt.team_cost = costs[i]
                receipt.team_place = places[i]
                receipt.team_body = contents[i]

                receipt.save()
        
        return redirect('party_detail', team_id)
    return redirect('party_detail', team_id)

