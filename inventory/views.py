from django.shortcuts import render
from inventory.models import Item
from django.views.generic.list import ListView


# Create your views here.
class ItemList(ListView):
    paginate_by = 20

    def get_template_names(self):
        if int(self.request.GET.get('page')) > 1:
            return ['_inventory_items.html']
        return ['inventory.html']

    def get_queryset(self):
        return Item.objects.all()
