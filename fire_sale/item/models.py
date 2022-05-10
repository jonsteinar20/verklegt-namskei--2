from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, blank=True)
    seller_username = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class offers(models.Model):
    nameOnCard = models.CharField(max_length=255)
    offer = models.FloatField()
    cardNum = models.FloatField()
    dateAndYear = models.FloatField()
    securityNum = models.FloatField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.nameOnCard
