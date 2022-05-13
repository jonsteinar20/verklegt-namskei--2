from django.forms import ModelForm
from item.models import Item, Offer
from user.models import Checkout

class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
