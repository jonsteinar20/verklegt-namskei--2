from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/contact_info // það sem er inni tomastrengnum
    path('', views.contact_info, name="checkout-contact_info"),
]