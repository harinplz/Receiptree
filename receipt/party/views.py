from django.shortcuts import render

from .models import *
# Create your views here.

# 파티 메인화면
def party_main(request):

    #GET으로 받아오기
    team_list = Team.objects.all() #팀 클래스 받아오기
    print(team_list)
    return render(request, 'party_06.html', {'team':team_list, })
