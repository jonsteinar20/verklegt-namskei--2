from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=9999)


    def __str__(self):
        return self.name
