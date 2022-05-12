from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from item.models import Item
from user.models import Profile


@login_required
def my_listings(request):
    profile = Profile.objects.filter(user=request.user).first()
    user_id = profile.user_id
    context = {'items': Item.objects.filter(seller=user_id).order_by('name')}
    return render(request, 'my_listings/index.html', context)