from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UploadFile(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d')


# Create your models here.

# class User(AbstractUser): #User Pass로만 설정
#     pass