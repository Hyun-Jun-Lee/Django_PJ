from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 모델 만들고 migrate 해줘야 적용
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=15, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)