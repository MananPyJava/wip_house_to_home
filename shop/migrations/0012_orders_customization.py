# Generated by Django 3.1.1 on 2020-09-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orders_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customization',
            field=models.CharField(default='', max_length=100),
        ),
    ]