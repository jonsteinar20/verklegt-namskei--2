from django.urls import path
from . import views

urlpatterns = [
    path('my_listings', views.index, name="my_listings"),
]