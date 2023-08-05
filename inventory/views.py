from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def index(request):
    context = {
        'categories': models.Category.objects.all()
    }
    return render(request, 'homegrid.html', context=context)
