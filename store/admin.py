from django.contrib import admin
from store.models import Products
from card.models import Order
from django.contrib.sessions.models import Session




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','surname','email']


admin.site.register(Products)