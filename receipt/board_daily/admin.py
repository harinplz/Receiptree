from django.contrib import admin

from .models import D_Board, D_Comment, D_Receipt

# Register your models here.
admin.site.register(D_Board)
admin.site.register(D_Comment)
admin.site.register(D_Receipt)