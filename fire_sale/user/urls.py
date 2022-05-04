from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users // það sem er inni tomastrengnum
    path('', views.index, name="user-index"),
]