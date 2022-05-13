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


class ContactInfo(models.Model):
    contact_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.PositiveIntegerField()

class Payment(models.Model):
    payment_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    card_number = models.PositiveIntegerField()
    exp_date = models.PositiveIntegerField()
    cvc = models.PositiveIntegerField()

class Review(models.Model):
    review_id = models.CharField(max_length=99)
    rating = models.PositiveIntegerField()

