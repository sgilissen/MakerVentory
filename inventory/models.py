from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.TextField(max_length=50)
    floor_plan = models.ImageField()

class ItemType(models.Model):
    name = models.TextField(max_length=50)

class Item(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_detail = models.TextField(max_length=50)
    photo = models.ImageField()
