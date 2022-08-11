from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#Board Class
class Board(models.Model):
    board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True)
    good_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank =True,
        related_name='good_user'
    )
    bad_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='bad_user'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def count_good_user(self):
        return self.good_user.count()

    def count_bad_user(self):
        return self.bad_user.count()



# Comment Class
class Comment(models.Model):
    board_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='board_no')
    user_no = models.ForeignKey('account.User', on_delete=models.CASCADE, db_column='user_no')
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"글 제목 - {self.board_no.title}, 내용 - {self.body}"



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
