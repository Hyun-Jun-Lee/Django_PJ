from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# on_delete=models.SET_NULL : user가 지워지면 알수 없음 게시물이 됨.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='article')
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)