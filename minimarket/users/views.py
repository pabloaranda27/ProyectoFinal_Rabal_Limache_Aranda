from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from users.forms import User_registration_form, Profile_update_form
from users.models import User_profile

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
            user=form.save()
            User_profile.objects.create(user=user)
            return redirect('login')
        else:
            context = {'error':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

def show_profile(request, username):
    user=User.objects.get(username=username)
    return render(request, 'users/show_profile.html', {'user':user})

def update_profile(request, username):
    user_id=request.user.id
    profile=User_profile.objects.get(user_id=user_id)
    user_basic_info=User.objects.get(id=user_id)
    if request.method == 'POST':
        form=Profile_update_form(request.POST, request.FILES)
        if form.is_valid():

            profile.image=form.cleaned_data.get('image')
            profile.phone=form.cleaned_data.get('phone')
            profile.address=form.cleaned_data.get('address')
            
            profile.save()
            return redirect(show_profile, username=request.user.username)

    elif request.method == 'GET':
        form=Profile_update_form()
        context={'form':form}
        return render (request,'users/update_profile.html',context=context)