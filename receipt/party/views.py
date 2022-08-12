from django.shortcuts import render

# Create your views here.

# 파티 메인화면
def party_main(request):
    return render(request, 'party_06.html')