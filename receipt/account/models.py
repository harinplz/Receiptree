from distutils.command.upload import upload
from email.mime import image
from email.policy import default
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
    image = models.ImageField(null=True, blank=True, upload_to = "", default="../static/img/default.png")
    team_no = models.ForeignKey('party.Team', on_delete=models.CASCADE, db_column='team_no', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True)

    job = models.CharField(max_length=40, null=True)
    age = models.IntegerField(null=True)
    income = models.IntegerField(null=True)
    expense = models.IntegerField(null=True) #지출 비용
    expense_body = models.TextField(null=True)

    written = models.IntegerField(null=True,default=0) #작성한 글 개수
    party_num = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return f"{self.username} - {self.nickname}"
    
    @property
    def my_image(self):
        if self.image:
            return self.image.url
        if not self.image:
            return f'../static/img/default.png'
        return ''


    
    
