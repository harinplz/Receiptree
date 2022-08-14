from calendar import week
from django.shortcuts import render

from board.models import Board
from party.models import Team
from account.models import User
from django.db.models import Count

from datetime import date, timedelta

# Create your views here.
def home(request):
    hot_list = Board.objects.annotate(num_good = Count('good_user')).order_by('-num_good')[:4]
    team_list = Team.objects.all()[:6] #팀 클래스 받아오기
    users = User.objects.all()
    
    #이번주 인기글 작성자 .. 

    #이번주 글 가져오기
    weekly_list = Board.objects.filter(date__range=[date.today() - timedelta(days=7), date.today() + timedelta(days=1) ])
    # 좋아요 순으로 정렬, 사용자만 가져오기
    weekly_list = weekly_list.annotate(num_good = Count('good_user')).order_by('-num_good')[:4]

    # 중복제거

    return render(request, 'home_04.html', {'hot':hot_list, 'team':team_list, 'weekly':weekly_list,})