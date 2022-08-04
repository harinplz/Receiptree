from django.db import models
from django.utils import timezone

# Create your models here.

# Team class
class Team(models.Model):
    team_no = models.AutoField(primary_key=True)
    category = models.IntegerField(blank=True) #0:절약 1:저축
    team_name = models.CharField(max_length=100)
    teammate_cnt = models.IntegerField(default=1) #팀원 수
    team1_no = models.IntegerField(null=True, blank=True)
    team2_no = models.IntegerField(null=True, blank=True)
    team3_no = models.IntegerField(null=True, blank=True)
    team4_no = models.IntegerField(null=True, blank=True)
    leader_no = models.IntegerField(null=True, blank=True)
    p_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    content = models.TextField()

    def __str__(self):
        return self.team_name


class Team_Board(models.Model):
    Team_board_no = models.AutoField(primary_key=True)
    Team_date = models.DateTimeField(default=timezone.now)
    Team_body = models.TextField()
    Team_good_cnt = models.IntegerField(default=0)
    Team_bad_cnt = models.IntegerField(default=0)
    team_no = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_no')


class Team_Comment(models.Model):
    Team_board_no = models.ForeignKey('Team_Board', on_delete=models.CASCADE, db_column='Team_board_no')
    Team_body = models.TextField()
    Team_date = models.DateTimeField(default=timezone.now)


class Team_Receipt(models.Model):
    Team_board_no = models.ForeignKey('Team_Board', on_delete=models.CASCADE, db_column='Team_board_no')
    #user_no는 마이페이지 기능과 연관
    Team_use_date = models.DateTimeField()
    Team_cost = models.IntegerField()
    Team_place = models.CharField(max_length=100)
    Team_body = models.TextField()