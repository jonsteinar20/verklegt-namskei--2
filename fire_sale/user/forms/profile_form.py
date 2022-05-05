from django.forms import ModelForm, widgets
from user.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'username' ]
        widgets = {
            'firstname': widgets.Select(attrs={ 'class': 'form-control' }),
            'lastname': widgets.TextInput(attrs={ 'class': 'form-control' })
        }