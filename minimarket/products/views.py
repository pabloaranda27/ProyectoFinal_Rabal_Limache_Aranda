from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Form_products

def new_product(request):
    if request.method == 'POST':
        form=Form_products(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                image=form.cleaned_data['image'],
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

def delete_prod(request, pk):
    if request.method == 'GET':
        product=Products.objects.get(pk=pk)
        context={'product':product}
        return render (request,'products/delete_products.html',context=context)
    elif request.method == 'POST':
        product=Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_products)

def update_prod(request, pk):
    if request.method == 'POST':
        form=Form_products(request.POST)
        if form.is_valid():
            product=Products.objects.get(pk=pk)
            product.name=form.cleaned_data['name']
            product.price=form.cleaned_data['price']
            product.description=form.cleaned_data['description']
            product.stock=form.cleaned_data['stock']
            product.save()
            return redirect(list_products)
    elif request.method == 'GET':
        product=Products.objects.get(id=pk)
        form=Form_products(initial={
            'name':product.name,
            'price':product.price,
            'description':product.description,
            'stock':product.stock,
        })
        context={'form':form}
        return render (request,'products/update_prod.html',context=context)