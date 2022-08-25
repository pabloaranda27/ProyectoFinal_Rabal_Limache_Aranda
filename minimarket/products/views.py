from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Form_products

def new_product(request):
    if request.method == 'POST':
        form=Form_products(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                stock=form.cleaned_data['stock'],
            )
            return redirect(list_products)
    elif request.method == 'GET':
        form=Form_products()
        context={'form':form}
        return render (request,'products/new_product.html',context=context)

def list_products(request):
    products=Products.objects.all()
    context={'products':products}
    return render (request,'products/list_products.html',context=context)

def search_products(request):
    search=request.GET['search']
    products=Products.objects.filter(name__icontains=search)
    context={'products':products}
    return render (request,'products/search_products.html',context=context)