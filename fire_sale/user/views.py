from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from user.models import User
from user.forms.profile_form import ProfileForm

<<<<<<< HEAD

#def index(request):
    #return render(request, 'user/index.html')
=======
def index(request):
<<<<<<< HEAD
    return render(request, 'user/index.html')
=======
    return render(request, 'user/index.html')
>>>>>>> 21e4bbaa02c9a206e40d96873dbeac72b698e39f

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

<<<<<<< HEAD
#def profile(request):
#    profile = Profile.objects.filter(user=request.user).first()
#    if request.method == 'POST':
#        form = ProfileForm(instance=profile, data=request.POST)
#        if form.is_valid():
#            profile = form.save(commit=False)
#            profile.user = request.user
#            profile.save()
#            return redirect('profile')
#    return render(request, 'user/profile.html', {
#        'form': ProfileForm(instance=profile)
#    })
>>>>>>> main
=======
def profile(request):
    profile = User.objects.filter(user=request.user).first()
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
>>>>>>> main
