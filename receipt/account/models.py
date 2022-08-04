from django.conf import settings
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
    image = models.ImageField(null=True)
    team_no = models.ForeignKey('party.Team', on_delete=models.CASCADE, db_column='team_no', null=True)


# User_info class 
class User_info(models.Model):
    user_no = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_no')
    job = models.CharField(max_length=40)
    age = models.IntegerField()
    income = models.IntegerField()
    expense = models.IntegerField() #지출 비용
    expense_body = models.TextField()
    
    
