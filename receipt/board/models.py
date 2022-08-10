from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.

#Board Class
class Board(models.Model):
    board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    good_cnt = models.IntegerField(default=0)
    bad_cnt = models.IntegerField(default=0)
    user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title



# Comment Class
class Comment(models.Model):
    board_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='board_no')
    user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)



# Receipt Class
class Receipt(models.Model):
    board_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='board_no')
    user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    use_date = models.CharField(max_length=50)
    cost = models.IntegerField()
    place = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"날짜: {self.use_date} , 비용: {self.cost}원, 장소: {self.place}"


# Tag Class
class Tag(models.Model):
    tagname = models.CharField(max_length=30)

    def __str__(self):
        return self.tagname
