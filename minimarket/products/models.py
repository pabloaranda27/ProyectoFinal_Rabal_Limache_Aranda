from distutils.command.upload import upload
from django.db import models

# class Categories(models.Model):
#     name=models.ForeignKey(Products, related_name='name')
    
class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.CharField(max_length=200, null=True, blank=True)
    is_available=models.BooleanField(default=True)
    image=models.ImageField(upload_to='products/', null=True, blank=True)
    creation_date=models.DateField(auto_now_add=True, null=True, blank=True)
    stock=models.IntegerField()
#    category=models.ForeignKey(Categories, related_name='name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'