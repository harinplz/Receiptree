from django.shortcuts import render

from board.models import Board
from party.models import Team
from django.db.models import Count

# Create your views here.
def home(request):
    hot_list = Board.objects.annotate(num_good = Count('good_user')).order_by('-num_good')[:4]
    team_list = Team.objects.all()[:6] #팀 클래스 받아오기
    
    return render(request, 'home_04.html', {'hot':hot_list, 'team':team_list})