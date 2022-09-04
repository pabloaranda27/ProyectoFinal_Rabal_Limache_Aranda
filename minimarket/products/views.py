from unicodedata import category
from django.shortcuts import render, redirect
from products.models import Products, Categories
from products.forms import Form_products, Form_categories
from django.contrib.auth.decorators import login_required

@login_required
def new_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form=Form_products(request.POST, request.FILES)
            if form.is_valid():
                Products.objects.create(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    image=form.cleaned_data['image'],
                    description=form.cleaned_data['description'],
                    stock=form.cleaned_data['stock'],
                    category=form.cleaned_data['category'],
                    )
                return redirect(list_products)
        elif request.method == 'GET':
            form=Form_products()
            context={'form':form}
            return render (request,'products/new_product.html',context=context)
    return redirect('login')

def list_products(request):
    products=Products.objects.all()
    context={'products':products}
    return render (request,'products/list_products.html',context=context)

def search_products(request):
    search=request.GET['search']
    products=Products.objects.filter(name__icontains=search)
    context={'products':products}
    return render (request,'products/search_products.html',context=context)

def detail_product(request, pk):
    if request.method == 'GET':
        product=Products.objects.get(pk=pk)
        context={'product':product}
        return render (request,'products/detail_product.html',context=context)

@login_required
def delete_product(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
            product=Products.objects.get(pk=pk)
            context={'product':product}
            return render (request,'products/delete_product.html',context=context)
        elif request.method == 'POST':
            product=Products.objects.get(pk=pk)
            product.delete()
            return redirect(list_products)
    return redirect('login')

@login_required
def update_product(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            form=Form_products(request.POST)
            if form.is_valid():
                product=Products.objects.get(pk=pk)
                product.name=form.cleaned_data['name']
                product.price=form.cleaned_data['price']
                product.description=form.cleaned_data['description']
                product.stock=form.cleaned_data['stock']
                product.category=form.cleaned_data['category']
                product.save()
                return redirect(list_products)
        elif request.method == 'GET':
            product=Products.objects.get(id=pk)
            form=Form_products(initial={
                'name':product.name,
                'price':product.price,
                'description':product.description,
                'stock':product.stock,
                'category':product.category,
            })
            context={'form':form}
            return render (request,'products/update_product.html',context=context)
    return redirect('login')

@login_required
def new_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form=Form_categories(request.POST, request.FILES)
            if form.is_valid():
                Categories.objects.create(
                    name=form.cleaned_data['name'],
                    image=form.cleaned_data['image'],
                    )
                return redirect(list_categories)
        elif request.method == 'GET':
            form=Form_categories()
            context={'form':form}
            return render (request,'products/new_category.html',context=context)
    return redirect('login')

def list_categories(request):
    categories=Categories.objects.all()
    context={'categories':categories}
    return render (request,'products/list_categories.html',context=context)
