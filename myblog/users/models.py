from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(max_length=30,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=100,verbose_name='密码')
    nickname = models.CharField(max_length=30,verbose_name='昵称')
    info = models.CharField(max_length=200,verbose_name='个人简介')
    sign = models.CharField(max_length=100,verbose_name='个性签名')
    avtar = models.ImageField(upload_to='head_img/%Y/%m',default='default.jpg')
