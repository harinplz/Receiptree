from django.contrib import admin

from .models import W_Board, W_Comment, W_Receipt

# Register your models here.
admin.site.register(W_Board)
admin.site.register(W_Comment)
admin.site.register(W_Receipt)