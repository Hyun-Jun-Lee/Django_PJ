from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project')
    image = models.ImageField(upload_to='project/', null=True)
    title = models.CharField(max_length=15, null=False)
    description = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # article 만들 때 프로젝트 이름 제대로 뜨게하기
    def __str__(self):
        return f'{self.pk} : {self.title}'