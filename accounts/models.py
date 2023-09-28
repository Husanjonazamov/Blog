from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    phone = models.IntegerField(null=True,blank=True)
    avatar = models.ImageField(upload_to="avatar/",default="avatar/default.jpg",blank=True)
    bio = models.CharField(max_length=255)
# Create your models here.
