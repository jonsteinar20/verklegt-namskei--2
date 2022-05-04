from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

items = [
    {'id': '1', 'name': 'iPhone 13 pro 64GB', 'price': 70000},
    {'id': '2', 'name': 'Designer glasses', 'price': 20000}
]

def index(request):
    return render(request, 'item/index.html', context={'items': items })