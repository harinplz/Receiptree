from unicodedata import category
from django.shortcuts import render

from .models import *
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


# 파티 만들기 화면
def party_make(request):
    return render(request, 'party_08.html')
