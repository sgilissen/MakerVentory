from django.urls import path
from . import views
from .views import HomePageView, search_view

app_name = 'inventory'
urlpatterns = [
    path('', search_view, name='items'),
    path('search/', search_view, name='items')
]
