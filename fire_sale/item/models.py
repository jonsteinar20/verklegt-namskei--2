from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)