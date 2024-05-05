from django.contrib import admin
from store.models import Products,CardItem,Card,Order
from django.contrib.sessions.models import Session




class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

class CardAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(Card, CardAdmin)
admin.site.register(CardItem)
admin.site.register(Products)
admin.site.register(Order)