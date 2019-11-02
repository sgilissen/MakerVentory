from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.TextField(max_length=50)
    floor_plan = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_detail = models.TextField(max_length=50)
    photo = models.ImageField(blank=True)
    in_stock = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.name


class ItemLinkType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ItemLink(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    link_type = models.ForeignKey(ItemLinkType, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.name
