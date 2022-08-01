from django.db import models
from django.utils import timezone

# Board class
class M_Board(models.Model):
    M_board_no = models.AutoField(primary_key=True)
    M_title = models.CharField(max_length=40)
    M_date = models.DateTimeField(default=timezone.now)
    M_body = models.TextField()
    M_good_cnt = models.IntegerField(default=0)
    M_bad_cnt = models.IntegerField(default=0)
    M_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')


    def __str__(self):
        return self.title


# Comment class
class M_Comment(models.Model):
    M_board_no = models.ForeignKey('M_Board', on_delete=models.CASCADE, db_column='M_board_no')
    M_name = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='name')
    M_body = models.TextField()
    M_date = models.DateTimeField(default=timezone.now)


# Receipt class
class M_Receipt(models.Model):
    M_board_no = models.ForeignKey('M_Board', on_delete=models.CASCADE, db_column='M_board_no')
    M_user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    M_use_date = models.DateTimeField()
    M_cost = models.IntegerField()
    M_place = models.CharField(max_length=100)
    M_body = models.TextField()