from django.forms import ModelForm
from django import forms
from item.models import Item
from django.forms import widgets


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'seller_username']
        widgets = {
            'name': widgets.textInput(attrs={'class': 'form-control'}),
            'description': widgets.textInput(attrs={'class': 'form-control'}),
            'price': widgets.numberInput(attrs={'class': 'form-control'}),
            'condition': widgets.textInput(attrs={'class': 'form-control'})
        }


