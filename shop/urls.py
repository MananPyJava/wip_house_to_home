from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.shop, name='shop'),
    path('buy', views.buy, name='buy'),
    path('check', views.check, name='check'),
]


HANDLER404='no_url'
HANDLER500='no_url'