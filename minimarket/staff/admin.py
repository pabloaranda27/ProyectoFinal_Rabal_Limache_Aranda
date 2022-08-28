from django.contrib import admin
from staff.models import Staff

@admin.register(Staff)
class Staff_admin(admin.ModelAdmin):
    list_display=['name','position','age']