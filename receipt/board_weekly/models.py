from django.db import models
from django.utils import timezone


# Board class
class W_Board(models.Model):
    W_board_no = models.AutoField(primary_key=True)
    W_title = models.CharField(max_length=40)
    W_date = models.DateTimeField(default=timezone.now)
    W_body = models.TextField()
    W_good_cnt = models.IntegerField(default=0)
    W_bad_cnt = models.IntegerField(default=0)
    W_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')


    def __str__(self):
        return self.title


# Comment class
class W_Comment(models.Model):
    W_board_no = models.ForeignKey('W_Board', on_delete=models.CASCADE, db_column='W_board_no')
    W_name = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='name')
    W_body = models.TextField()
    W_date = models.DateTimeField(default=timezone.now)


# Receipt class
class W_Receipt(models.Model):
    W_board_no = models.ForeignKey('W_Board', on_delete=models.CASCADE, db_column='W_board_no')
    W_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    W_use_date = models.DateTimeField()
    W_cost = models.IntegerField()
    W_place = models.CharField(max_length=100)
    W_body = models.TextField()