from django.contrib import admin
from django.urls import path
from home import views
from board import views as board_views
from account import views as account_views
from django.conf import settings #settings.py import
from django.conf.urls.static import static # 'static' import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('board/', board_views.board_main, name='board_main'),
    path('board/write', board_views.board_write, name='board_write'),
    path('board/detail/<int:board_id>', board_views.board_detail, name='board_detail'),
    path('newcomment/<int:board_id>', board_views.new_comment, name='new_comment'),
    path('good/', board_views.board_good, name='board_good'),
    path('bad/', board_views.board_bad, name='board_bad'),
    path('mypage', account_views.mypage, name='mypage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
