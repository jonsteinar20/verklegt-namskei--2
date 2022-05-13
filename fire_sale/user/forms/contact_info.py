from django.forms import ModelForm, widgets
from user.models import ContactInfo

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ['contact_id']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
