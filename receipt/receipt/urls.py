from django.contrib import admin
from django.urls import path
from home import views
from board import views as board_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('board/', board_views.board, name='board'),
    path('board/write', board_views.write, name='board_write'),
    path('mypage', account_views.mypage, name='mypage'),
    path('signup', account_views.signup, name='signup'),
]
