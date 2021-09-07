from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')
    # user-project 한 쌍이 가지는 subscription은 하나만 존재하도록 설정
    class Meta:
        unique_together=('user', 'project')