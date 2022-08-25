from django.views.generic import CreateView, ListView

from django.shortcuts import render
from stores.models import Stores

class List_stores(ListView):
    model= Stores
    template_name= 'stores/list_stores.html'

class New_store(CreateView):
    model= Stores
    template_name= 'stores/new_store.html'
    fields = '__all__'
    success_url = '/stores/list-stores/'