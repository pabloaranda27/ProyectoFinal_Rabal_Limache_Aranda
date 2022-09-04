from django import forms
from products.models import Categories

class Form_products(forms.Form):
    image=forms.ImageField(required=False)
    name=forms.CharField(max_length=30)
    price=forms.FloatField()
    description=forms.CharField(max_length=300, widget=forms.Textarea)
    stock=forms.IntegerField()
    category=forms.ModelChoiceField(queryset=Categories.objects.all())

class Form_categories(forms.Form):
    image=forms.ImageField(required=False)
    name=forms.CharField(max_length=70)