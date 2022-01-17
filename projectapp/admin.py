from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project)
class Projectadmin(admin.ModelAdmin):
    list_display = ['writer','image','title',]
