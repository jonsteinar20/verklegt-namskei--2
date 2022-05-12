from django.urls import path
from . import views

urlpatterns = [
    path('my_listings', views.my_listings, name="my_listings"),
    ]