from django.contrib import admin
from .models import Team, Team_Board, Team_Comment, Team_Receipt

# Register your models here.
admin.site.register(Team)
admin.site.register(Team_Board)
admin.site.register(Team_Comment)
admin.site.register(Team_Receipt)