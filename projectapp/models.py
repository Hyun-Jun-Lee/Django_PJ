from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project')
    image = models.ImageField(upload_to='project/', null=True)
    title = models.CharField(max_length=15, null=False)
    description = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)