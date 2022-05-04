
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    #if 'search_filter' in request.GET:
        #search_filter = request.GET('search_filter')
        #item = [ {
         #   'id': x.id,
        #    'name': x.name,
        #    'description': x.description
        #} for x in Item.objects.filter(name__icontains=search_filter) ]
    return render(request, 'user/index.html')

#def get_item_by_id(request, id):
    #return render(request, 'item/item_details.html', {
    #    'item': get_object_or_404(Item, pk=id)
    #})