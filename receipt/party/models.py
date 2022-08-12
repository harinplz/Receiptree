from pyexpat import model
from django.db import models
from django.utils import timezone

from django.conf import settings

# Create your models here.

# Team class
class Team(models.Model):
    team_no = models.AutoField(primary_key=True)
    category = models.CharField(null=True, blank=True, max_length=30) # '절약' '저축' 중 하나
    team_name = models.CharField(max_length=100)
    content = models.TextField()

    #팀원 구현 수정 -> 다대다 관계로 가져오기
    team_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='team_users',
    )
    # teammate_cnt = models.IntegerField(default=1) #팀원 수
    # team1_no = models.IntegerField(null=True, blank=True)
    # team2_no = models.IntegerField(null=True, blank=True)
    # team3_no = models.IntegerField(null=True, blank=True)
    # team4_no = models.IntegerField(null=True, blank=True)

    # 리더 멤버 지정 수정 -> 외래키로 가져오기
    leader_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='leader_no', null=True)
    #leader_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.team_name

    # 팀원 수 세는 함수
    def count_team_users(self):
        return self.team_users.count()


# 팀 게시판 클래스
class Team_Board(models.Model):
    team_board_no = models.AutoField(primary_key=True)

    team_date = models.DateTimeField(default=timezone.now)
    team_body = models.TextField()

    # 팀 글 좋아요/나빠요 구현 수정 -> 다대다 관계로
    team_good_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='team_good_user'
    )
    team_bad_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name = 'team_bad_user'
    )
    # Team_good_cnt = models.IntegerField(default=0)
    # Team_bad_cnt = models.IntegerField(default=0)
    team_no = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_no')
    team_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='team_user_no', null=True)

    # 글 올린 최신순으로 정렬
    class Meta:
        ordering=['-team_date']

    def __str__(self):
        return self.team_board_no.team_name

    # 좋아요 누른 유저 수 카운트
    def count_team_good_users(self):
        return self.team_good_users.count()

    # 나빠요 누른 유저 수 카운트
    def count_team_bad_users(self):
        return self.team_bad_users.count()


# 팀 댓글 클래스
class Team_Comment(models.Model):
    team_board_no = models.ForeignKey('Team_Board', on_delete=models.CASCADE, db_column='team_board_no', null=True)
    team_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='team_user_no', null=True)
    team_body = models.TextField()
    team_date = models.DateTimeField(default=timezone.now)


class Team_Receipt(models.Model):
    team_board_no = models.ForeignKey('Team_Board', on_delete=models.CASCADE, db_column='team_board_no', null=True)
    #user_no는 마이페이지 기능과 연관
    team_use_date = models.DateTimeField()
    team_cost = models.IntegerField()
    team_place = models.CharField(max_length=100)
    team_body = models.TextField()