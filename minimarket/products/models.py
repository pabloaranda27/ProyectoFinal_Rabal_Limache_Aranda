from distutils.command.upload import upload
from django.db import models

class Categories(models.Model):
    image=models.ImageField(upload_to='categories/', null=True, blank=True)
    name=models.CharField(max_length=70)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'    

class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.TextField(null=True, blank=True)
    is_available=models.BooleanField(default=True)
    image=models.ImageField(upload_to='products/', null=True, blank=True)
    creation_date=models.DateField(auto_now_add=True, null=True, blank=True)
    stock=models.IntegerField()
    category=models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'