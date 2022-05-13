from django.forms import ModelForm, widgets
from payment.models import PaymentInfo

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInputInput(attrs={'class': 'form-control'})
        }