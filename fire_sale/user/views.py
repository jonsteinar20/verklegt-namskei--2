from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
from user.forms.signup_form import SignUpForm
from item.forms.make_bid_form import MakeBidForm
from item.models import Item, Offer
from item.views import make_bid
from django.contrib.auth.decorators import login_required
from user.forms.contact_info import ContactInfoForm
from user.forms.payment import PaymentForm


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

@login_required
def my_bids(request):
    profile = Profile.objects.filter(user=request.user).first()
    user_id = profile.user_id
    context = {'items' : Item.objects.filter(offer__buyer_id = user_id)}
    return render(request, 'user/my_bids.html', context)


def contact_info(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ContactInfoForm()
    return render(request, 'user/contact_info.html', {
        'form' : form
    })

def payment(request):
    if request.method == 'POST':
        print(1)
    else:
        form = PaymentForm()
    return render(request, 'user/payment.html', {
        'form' : form
    })



