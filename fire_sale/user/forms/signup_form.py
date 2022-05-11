from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter the same password as before, for verification.'
        self.fields['username'].widget.attrs['placeholder'] = 'Max length is 32'
        self.fields['username'].help_text = ''
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
