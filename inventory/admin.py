from django.contrib import admin
from inventory.models import Location, Area, Container, Category, ItemType, ItemManufacturer, Item


# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ...


@admin.register(Area)
class RoomAdmin(admin.ModelAdmin):
    ...


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(ItemManufacturer)
class ItemManufacturerAdmin(admin.ModelAdmin):
    ...


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...


