from django.db import models

class Staff(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    position=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    store=models.CharField(max_length=50)
    date_of_hired=models.DateField(auto_now_add=True, null=True, blank=True)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Staff'
        verbose_name_plural='Staff'