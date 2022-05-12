from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
from user.forms.signup_form import SignUpForm
from item.forms.make_bid_form import MakeBidForm
from item.models import Item, Offer
from item.views import make_bid


#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('login')
#    return render(request, 'user/register.html', {
#        'form': UserCreationForm()
#    })

def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        error_msg = form.errors.values
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors': error_msg, 'form': SignUpForm()}
            return render(request, 'user/register.html', context)
    return render(request, 'user/register.html', {
        'form': SignUpForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })

def my_bids(request):
    if request.method == 'GET':
        return render(request, 'user/my_bids.html')
