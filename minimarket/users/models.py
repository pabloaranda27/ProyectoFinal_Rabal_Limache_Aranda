from django.db import models

class User_profile(models.Model):
    image=models.ImageField(upload_to='profile_image/', blank=True)
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.CharField(max_length=20, blank=True)
    address=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username + ' Profile'

    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profiles'