from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request, 'receipt_01.html')


def write(request):
    return render(request, 'write_02.html')
