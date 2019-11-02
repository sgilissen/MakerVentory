from django.urls import path
from . import views

#GigsList.as_view(name='gigs')
app_name = 'inventory'
urlpatterns = [
    path('', views.ItemList)
]