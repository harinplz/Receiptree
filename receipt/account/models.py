from django.db import models
from django.contrib.auth.models import AbstractUser

#User class
class User(AbstractUser):
    user_no = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=40)
    #username 기본제공
    #password django 기본 제공
    #email 기본 제공
    notify_cnt = models.IntegerField(default=0)
    grade = models.CharField(max_length=40)
    team_no = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_no')


# User_info class 
class User_info(models.Model):
    user_no = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_no', primary_key=True)
    job = models.CharField(max_length=40)
    age = models.IntegerField()
    income = models.IntegerField()
    expense = models.IntegerField() #지출 비용
    expense_body = models.TextField()
    
    
