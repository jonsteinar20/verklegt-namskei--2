from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users // það sem er inni tomastrengnum
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('my_bids', views.my_bids, name='my_bids'),
    path('contact_info', views.contact_info, name='contact_info'),
    path('payment', views.payment, name='payment')

]