from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from item.models import Item, ItemImage
from item.forms.item_form import ItemCreateForm
# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.itemimage_set.first().image
        } for x in Item.objects.filter(name__contains=search_filter) ]
        return JsonResponse({ 'data': items })
    context = { 'items': Item.objects.all().order_by('name') }
    return render(request, 'item/index.html', context)


def filter_by_price(request):
    context = { 'items': Item.objects.all().order_by('-price') }
    return render(request, 'item/index.html', context)


def filter_by_name(request):
    context = { 'items': Item.objects.all().order_by('name') }
    return render(request, 'item/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'item/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })


@login_required
def create_item(request):
    if request.method == 'POST':
        print(1)
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('item-index')
    else:
        form = ItemCreateForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })

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

def make_bid(request):
    return