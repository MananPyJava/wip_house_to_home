from django.db import models

# Create your models here.
class shop_items(models.Model):
    name_of_item=models.CharField(max_length=1000)
    image_url=models.CharField(max_length=10000)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)

class orders(models.Model):
    name=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    email=models.EmailField(max_length=50)
    ordered_item=models.CharField(max_length=100, default='')
    phone_number=models.IntegerField(default=0)