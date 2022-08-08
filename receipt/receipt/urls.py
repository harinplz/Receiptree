from django.contrib import admin
from django.urls import path
from home import views
from board import views as board_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('board/', board_views.board, name='board'),
]
