from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory.html', {'items': items})


class HomePageView(TemplateView):
    template_name = 'home.html'


class ItemViewDetail(TemplateView):
    template_name = 'item_detail.html'


def search_view(request):
    ctx = {}
    url_param = request.GET.get("q")

    if url_param:
        items = Item.objects.filter(name__icontains=url_param)
    else:
        items = Item.objects.all()

    ctx["items"] = items

    if request.is_ajax():
        html = render_to_string(
            template_name = "search-partial.html",
            context = {"items": items}
        )

        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "search_results.html", context=ctx)

def item_view_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    return render(request, 'item_detail.html', {'item': item})
