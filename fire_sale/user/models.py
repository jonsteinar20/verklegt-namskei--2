from django.contrib.auth.models import User
from user.views import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, on_delete=models.CASCADE)
    bio = models.ForeignKey(max_length=255, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    #username = models.CharField(max_length=255)
    #firstname = models.CharField(max_length=255)
    #lastname = models.CharField(max_length=255)
    #password = models.CharField(max_length=255)
    #email = models.CharField(max_length=255)

    def __str__(self):
        self.name

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name