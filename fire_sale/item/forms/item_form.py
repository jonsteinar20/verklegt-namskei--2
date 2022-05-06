from django.forms import ModelForm, widgets
from django import forms
from item.models import Item


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.textInput(attrs={'class': 'form-control'}),
            'description': widgets.textInput(attrs={'class': 'form-control'}),
            'category': widgets.textInput(attrs={'class': 'form-control'}),
            'price': widgets.numberInput(attrs={'class': 'form-control'}),
            #'condition': widgets.textInput(attrs={'class': 'form-control'}),
            'seller_username': widgets.textInput(attrs={'class': 'form-control'})
        }


