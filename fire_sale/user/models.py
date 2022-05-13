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

class Checkout(models.Model):
    full_name = models.CharField(max_length=999)
    address = models.CharField(max_length=999)
    city = models.CharField(max_length=999)
    country = models.CharField(max_length=999)
    postal_code = models.CharField(max_length=999)
    name_on_card = models.CharField(max_length=999)
    card_number = models.PositiveIntegerField(max_length=16)
    exp_date = models.PositiveIntegerField(max_length=4)
    cvc = models.PositiveIntegerField(max_length=3)