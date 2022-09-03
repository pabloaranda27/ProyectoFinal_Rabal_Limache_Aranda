from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from users.models import User_profile

class User_registration_form(UserCreationForm):
    username=forms.CharField(label='Usuario', max_length=50)
    first_name=forms.CharField(label='Nombre', max_length=50)
    last_name=forms.CharField(label='Apellido', max_length=50)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class Profile_update_form(forms.Form):
    image=forms.ImageField()
    phone=forms.CharField(max_length=20)
    address=forms.CharField(max_length=200)

    class Meta:
        model = User_profile
        fields = ('image', 'phone', 'address')