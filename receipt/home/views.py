from django.shortcuts import render

from board.models import Board
from django.db.models import Count

# Create your views here.
def home(request):
    hot_list = Board.objects.annotate(num_good = Count('good_user')).order_by('-num_good')[:4]
    
    return render(request, 'home_04.html', {'hot':hot_list})