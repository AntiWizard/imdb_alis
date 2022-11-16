from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    birth_day = models.DateField()
    username = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='movies/avatars/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
