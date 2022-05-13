from django.db import models

class ContactInfo(models.Model):
    full_name = models.CharField(max_length=999)
    address = models.CharField(max_length=999)
    city = models.CharField(max_length=999)
    country = models.CharField(max_length=999)
    postal_code = models.IntegerField()
