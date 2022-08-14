from django.contrib import admin
from django.urls import path
from home import views
from board import views as board_views
from account import views as account_views
from party import views as party_views
from django.conf import settings #settings.py import
from django.conf.urls.static import static # 'static' import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #게시판
    path('board/', board_views.board_main, name='board_main'),
    path('board/write', board_views.board_write, name='board_write'),
    path('board/detail/<int:board_id>', board_views.board_detail, name='board_detail'),
    path('newcomment/<int:board_id>', board_views.new_comment, name='new_comment'),
    path('good/', board_views.board_good, name='board_good'),
    path('bad/', board_views.board_bad, name='board_bad'),
    #마이페이지
    path('mypage', account_views.mypage, name='mypage'),
    path('mypage_change', account_views.mypage_change, name='mypage_change'),
    path('signup', account_views.signup, name='signup'),
    path('login', account_views.login, name='login'),
    path('logout', account_views.logout, name='logout'),
    path('signout', account_views.signout, name='signout'),
    path('view_receipt', account_views.view_receipt, name='view_receipt'),
    path('view_party', account_views.view_party, name='view_party'),
    #파티
    path('party/', party_views.party_main, name='party_main'),
    path('party/frugality', party_views.party_main_fru, name='party_main_fru'), #절약 카테고리
    path('party/saving', party_views.party_main_saving, name='party_main_saving'), #저축 카테고리
    path('party/detail/<int:team_id>', party_views.party_detail, name='party_detail'), # 파티 상세화면
    path('newcomment_party/<int:team_id>', party_views.newcomment_party, name='newcomment_party'), #파티댓글
    # path('party_good/', party_views.party_good, name="party_good"),
    # path('party_bad/', party_views.party_bad, name="party_bad"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
