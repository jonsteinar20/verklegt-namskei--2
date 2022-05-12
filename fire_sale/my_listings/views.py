from django.shortcuts import render
from item.models import Item
from user.models import Profile
# Create your views here.


def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    user_id = profile.user_id
    context = {'items': Item.objects.filter(seller = user_id).order_by('name')}
    return render(request, 'my_listings/index.html', context)