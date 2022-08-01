from django.db import models
from django.utils import timezone

# Create your models here.

# Board class
class D_Board(models.Model):
    D_board_no = models.AutoField(primary_key=True)
    D_title = models.CharField(max_length=40)
    D_date = models.DateTimeField(default=timezone.now)
    D_body = models.TextField()
    D_good_cnt = models.IntegerField(default=0)
    D_bad_cnt = models.IntegerField(default=0)
    D_name = models.ForeignKey('User', on_delete=models.CASCADE, db_column='name')
    D_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')


    def __str__(self):
        return self.D_title


# Comment class
class D_Comment(models.Model):
    D_board_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='D_board_no')
    D_name = models.ForeignKey('User', on_delete=models.CASCADE, db_column='name')
    D_body = models.TextField()
    D_date = models.DateTimeField(default=timezone.now)


# Receipt class
class D_Receipt(models.Model):
    D_board_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='D_board_no')
    D_user_no = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_no')
    D_use_date = models.DateTimeField()
    D_cost = models.IntegerField()
    D_place = models.CharField(max_length=100)
    D_body = models.TextField()