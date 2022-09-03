from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    image=models.ImageField(upload_to='profile/', null=True, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone=models.CharField(max_length=20, null=True, blank=True)
    address=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username + ' Profile'

    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profiles'