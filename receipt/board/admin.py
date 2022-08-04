from xml.etree.ElementTree import Comment
from django.contrib import admin

from .models import Board, Comment, Receipt, Tag

# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Receipt)
admin.site.register(Tag)