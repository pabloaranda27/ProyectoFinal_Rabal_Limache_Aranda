from django.contrib import admin
from stores.models import Stores

@admin.register(Stores)
class Stores_admin(admin.ModelAdmin):
    list_display=['name','address','city','manager']