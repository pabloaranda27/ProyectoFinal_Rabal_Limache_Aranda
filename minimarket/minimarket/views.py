from django.shortcuts import render

def home(request):
    return render(request,'index.html',context={})

def base(request):
    return render(request,'base.html',context={})