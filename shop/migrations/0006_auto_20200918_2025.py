# Generated by Django 2.2.7 on 2020-09-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200918_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_items',
            name='image_url',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
