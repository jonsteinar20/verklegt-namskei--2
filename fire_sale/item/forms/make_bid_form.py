from django.forms import ModelForm, widgets
from item.models import Offer


class MakeBidForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id', 'item', 'buyer']
        widgets = {
            'amount': widgets.NumberInput(attrs={ 'class': 'form-control' })
        }



