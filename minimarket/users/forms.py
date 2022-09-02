from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from users.models import User_profile

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {k:'' for k in fields}

class User_profile_form(forms.Form):
    image=forms.ImageField()
    name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phone=forms.CharField(max_length=20)
    address=forms.CharField(max_length=200)

    class Meta:
        model = User_profile
        fields = ('image', 'name', 'last_name', 'age', 'phone', 'address')
