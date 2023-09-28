from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser




class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    # image = models.ImageField(upload_to="posts/")

    
    def __str__(self):
        return self.title

# Create your models here.

    
    def get_absolute_url(self):
        return reverse("post_detail",args=[str(self.pk)])
    
