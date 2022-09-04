from django.contrib import admin
from products.models import Products, Categories

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display=['name','price','stock']

@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    list_display=['name']