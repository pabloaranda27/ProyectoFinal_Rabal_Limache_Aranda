from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import User_registration_form, User_profile_form
from users.models import User_profile
from products.views import list_products

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':'Usted a ingresado con exito a la web!'}
                return render(request, 'index.html', context = context)
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Usuario y/o contraseña incorrectos', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'error':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

# def profile(request, pk):
#     profile=User_profile.objects.get(pk=pk)
#     context={'profile':profile}
#     return render (request,'users/profile.html',context=context)

def create_profile(request):
    if request.method == 'POST':
        form=User_profile_form(request.POST, request.FILES)
        if form.is_valid():
            User_profile.objects.create(
                image=form.cleaned_data['image'],
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                age=form.cleaned_data['age'],                
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                )
            return redirect(list_products)
    elif request.method == 'GET':
        form=User_profile_form()
        context={'form':form}
        return render (request,'users/create_profile.html',context=context)