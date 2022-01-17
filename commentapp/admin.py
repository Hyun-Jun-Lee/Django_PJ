from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['article','writer','content']
