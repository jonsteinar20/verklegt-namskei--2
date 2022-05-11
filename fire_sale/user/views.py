from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from user.models import Profile
from user.forms.profile_form import ProfileForm
from user.forms.signup_form import SignUpForm


def index(request):
    return render(request, 'user/index.html')


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
    profile = Profile.objects.get(user=request.user).first()
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
