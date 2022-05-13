from django.db import models

class PaymentInfo(models.Model):
    full_name = models.CharField(max_length=999)
    card_number = models.IntegerField()
    exp_date = models.IntegerField()
    cvc = models.IntegerField()
from django.db import models

# Create your models here.
