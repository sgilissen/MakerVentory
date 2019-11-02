from django.contrib import admin
from .models import Location, Item, ItemType, ItemLink, ItemLinkType
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ItemLinkInline(admin.TabularInline):
    model = ItemLink
    extra = 0


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ItemLinkType)
class ItemLinkTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'location', 'location_detail', 'in_stock')
    search_fields = ['name']
    list_filter = ('item_type', 'location')
    inlines = [ItemLinkInline]
