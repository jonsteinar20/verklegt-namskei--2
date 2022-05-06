from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

items = [
    {'id': '1', 'name': 'iPhone 13 pro 64GB', 'price': 70000},
    {'id': '2', 'name': 'Designer glasses', 'price': 20000}
]
def index(request):
    #if 'search_filter' in request.GET:
        #search_filter = request.GET('search_filter')
        #items = [ {
         #   'id': x.id,
        #    'name': x.name,
        #    'description': x.description
        #} for x in Item.objects.filter(name__icontains=search_filter) ]
        #return JsonResponse({ 'data': items })
    #context = { 'items': Item.objects.all().order_by('name') }

    return render(request, 'user/index.html')

    return render(request, 'item/index.html', context={ 'items':items })


#def get_item_by_id(request, id):
    #return render(request, 'item/item_details.html', {
    #    'item': get_object_or_404(Item, pk=id)
    #})

#def create_item(request):
    #if request.method == 'POST':
        #form = ItemCreateForm(data=request.POST)
        #if form.is_valid():
            #item = form.save()
            #return redirect('item-index')
    #else:
        #form = ItemCreateForm()
    #return render(request, 'item/create_item.html', {
        #'form': form
    #})

#def delete_item(request, id):
    #item = get_object_or_404(Item, pk=id)
    #item.delete()
    #return redirect('item-index')

#def update_item(request, id):
    #instance = get_object_or_404(Item, pk=id)
    #if request.method == 'POST':
        #form = ItemUpdateForm(data=request.POST, instance=instance)
        #if form.is_valid():
            #form.save()
            #return redirect('item_details', id=id)
    #else:
        #form = ItemUpdateForm(instance=instance)
    #return render(request, 'item/item_update.html', {
        #'form': form,
        #'id': id

    #})

    #})
