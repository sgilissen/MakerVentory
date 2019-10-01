from django.contrib import admin
from .models import Location, Item, ItemType
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def datasheet_link(self, obj):
        if obj.data_sheet == '':
            return('None')
        else:
            return mark_safe('<a href="%s">%s %s</a>' % (obj.data_sheet, obj.name, "datasheet"))

    list_display = ('name', 'item_type', 'location', 'location_detail', 'datasheet_link')
    search_fields = ['name']
    list_filter = ('item_type', 'location')


