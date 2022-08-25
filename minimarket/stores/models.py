from django.db import models

class Stores(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    manager=models.CharField(max_length=30)
    open_time=models.TimeField()
    close_time=models.TimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Store'
        verbose_name_plural='Stores'
