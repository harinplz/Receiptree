from django.contrib import admin

from .models import M_Board, M_Comment, M_Receipt

# Register your models here.
admin.site.register(M_Board)
admin.site.register(M_Comment)
admin.site.register(M_Receipt)