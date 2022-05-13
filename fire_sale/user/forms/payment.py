from django.forms import ModelForm, widgets
from user.models import Payment

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['payment_id']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
