from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/items // það sem er inni tomastrengnum
    path('', views.index, name="item-index"),
    path('<int:id>', views.get_item_by_id, name="item_details"),
    #path(r'^$', views.get_item_by_id, name="item_details"),
    path('create_item', views.create_item, name="create_item")
    #path('', views.index, name="item-categories")
]