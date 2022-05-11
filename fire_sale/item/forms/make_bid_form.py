from django.forms import ModelForm, widgets
from item.models import Offer


class MakeBidForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id']
        widgets = {
            'amount': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'})
        }



