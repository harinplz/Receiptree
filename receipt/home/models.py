from django.db import models
# Create your models here.


# Team class
class Team(models.Model):
    team_no = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    team_name = models.CharField(max_length=100, unique=True)
    teammate_cnt = models.IntegerField() #팀원 수
    teammate_limit = models.IntegerField() #제한인원 수
    content = models.TextField()

    def __str__(self):
        return self.team_name

