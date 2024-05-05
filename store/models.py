from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
import os
from django.contrib.sessions.models import Session
import json


def generater_path(instance,filename):
    return os.path.join(instance.slug,filename)
    
    
class Products(models.Model):
    CATEGORY_CHOICES = [
        ('No sugar', 'No sugar'),
        ('Fruit', 'Fruit'),
        ('Original', 'Original'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=100)
    price = models.FloatField()
    preview = models.ImageField(upload_to=generater_path)
    quantity = models.IntegerField(default=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.title    
    
    
@receiver(pre_save, sender=Products)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        




class Card(models.Model):
    session_user=models.CharField(max_length=100,unique=True)


class CardItem(models.Model):
    card=models.ForeignKey(Card, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Products, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.title
    


class Order(models.Model):
    city = models.TextField()
    street = models.TextField()
    home = models.TextField()
    flot = models.CharField(max_length=20)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    shopping_list = models.TextField(null=True)







    