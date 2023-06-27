# Generated by Django 4.2.2 on 2023-06-27 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_item_in_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemmanufacturer',
            options={'verbose_name': 'manufacturer', 'verbose_name_plural': 'manufacturers'},
        ),
        migrations.AlterField(
            model_name='container',
            name='map_location_x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='map_location_y',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]