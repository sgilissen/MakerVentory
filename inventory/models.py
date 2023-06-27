from django.db import models


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=200)
    street_name = models.CharField(blank=True, max_length=250)
    number = models.CharField(blank=True, max_length=5)
    postal_code = models.CharField(blank=True, max_length=10)
    municipality = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.location_name}"

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'


class Area(models.Model):
    area_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    map = models.FileField(blank=True, help_text="Optional top-down image of the area")

    def __str__(self):
        return f"{self.area_name}"

    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'


class Container(models.Model):
    container_name = models.CharField(max_length=250)
    container_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    map_location_x = models.IntegerField(blank=True, null=True)
    map_location_y = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Container {self.container_name} in {self.container_area}"

    class Meta:
        verbose_name = 'container'
        verbose_name_plural = 'containers'


class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ItemType(models.Model):
    type = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.type}"

    class Meta:
        verbose_name = 'item type'
        verbose_name_plural = 'item types'


class ItemManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=250)
    manufacturer_url = models.URLField(max_length=250, blank=True, verbose_name="Manufacturer URL")

    def __str__(self):
        return f"{self.manufacturer_name}"

    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'


class Item(models.Model):
    ITEM_STATUS_CHOICES = [
        ("NA", "Not Applicable"),
        ("WK", "Working"),
        ("DE", "Defective"),
        ("RE", "In Repair"),
        ("TE", "In Test"),
        ("LO", "Loaned out"),
        ("MS", "Missing"),
        ("ST", "Stolen")
    ]
    item_name = models.CharField(max_length=250)
    item_status = models.CharField(choices=ITEM_STATUS_CHOICES, default="NA", max_length=5)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE, blank=True, null=True)
    item_manufacturer = models.ForeignKey(ItemManufacturer, on_delete=models.CASCADE, blank=True, null=True)
    model_name = models.CharField(max_length=100, blank=True)
    item_support_url = models.URLField(max_length=250, blank=True, verbose_name="Support URL")
    datasheet_url = models.URLField(max_length=250, blank=True, verbose_name="Datasheet URL")
    owner_name = models.CharField(max_length=250, blank=True)  # For usage in more "public" settings, e.g. Hackerspaces
    in_use_by = models.CharField(max_length=250, blank=True)  # For usage in more "public" settings, e.g. Hackerspaces
    notes = models.TextField(max_length=10000, blank=True)
    in_stock = models.BooleanField(default=False)
    current_stock = models.IntegerField(blank=True, null=True)
    order_url = models.URLField(max_length=250, blank=True, verbose_name="Webshop/order URL")
    last_update = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        # Quick join on a list comprehension to elegantly concatenate manufacturer + item name with proper spaces
        return ' '.join([i for i in [f'{self.item_manufacturer}', f'{self.item_name}'] if i != 'None'])
