# Generated by Django 2.2.7 on 2020-09-16 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200916_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop_items',
            old_name='image',
            new_name='image_url',
        ),
    ]
