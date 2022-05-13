from django.db import models
from user.models import Profile
from django.contrib.auth.models import User


# Create your models here.
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, blank=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    highest_offer = models.PositiveIntegerField(default=0, editable=True)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Offer(models.Model):
    amount = models.PositiveIntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
