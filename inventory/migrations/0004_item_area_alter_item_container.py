# Generated by Django 4.2.2 on 2023-06-27 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_area_options_rename_areaname_area_area_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.area'),
        ),
        migrations.AlterField(
            model_name='item',
            name='container',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.container'),
        ),
    ]