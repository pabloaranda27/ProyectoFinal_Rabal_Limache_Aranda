from django import forms

class Form_products(forms.Form):
    image=forms.ImageField(required=False)
    name=forms.CharField(max_length=30)
    price=forms.FloatField()
    description=forms.CharField(max_length=200)
    stock=forms.IntegerField()