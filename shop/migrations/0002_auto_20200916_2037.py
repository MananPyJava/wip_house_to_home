# Generated by Django 2.2.7 on 2020-09-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_items',
            name='image',
            field=models.CharField(max_length=10000),
        ),
    ]