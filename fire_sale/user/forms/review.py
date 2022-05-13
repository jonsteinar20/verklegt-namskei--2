from django.forms import ModelForm, widgets
from user.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['review_id']
        widgets = {
            'rating': widgets.NumberInput(attrs={ 'class': 'form-control'}),

        }
