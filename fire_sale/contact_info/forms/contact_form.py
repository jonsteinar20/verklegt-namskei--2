from django.forms import ModelForm, widgets
from contact_info.models import ContactInfo
from user.models import Checkout

class ContactForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'})
        }