from django.db import models

# Create your models here.

# Team class
class Team(models.Model):
    team_no = models.AutoField(primary_key=True)
    category = models.IntegerField() #0:절약 1:저축
    team_name = models.CharField(max_length=100, unique=True)
    teammate_cnt = models.IntegerField() #팀원 수
    team1_no = models.IntegerField(null=True)
    team2_no = models.IntegerField(null=True)
    team3_no = models.IntegerField(null=True)
    team4_no = models.IntegerField(null=True)
    leader_no = models.IntegerField(null=True)
    p_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    content = models.TextField()

    def __str__(self):
        return self.team_name