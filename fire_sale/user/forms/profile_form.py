from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'bio': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' })
        }