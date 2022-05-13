from django.forms import ModelForm
from django import forms
from item.models import Item
from django.forms import widgets


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item

        exclude = ['id','highest_offer']

        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

