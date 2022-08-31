from urllib import request
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

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

class Detail_stores(DetailView):
    model= Stores
    template_name= 'stores/detail_stores.html'

class Delete_stores(DeleteView):
    model= Stores
    template_name= 'stores/delete_stores.html'
    success_url = '/stores/list-stores/'

class Update_stores(UpdateView):
    model= Stores
    template_name= 'stores/update_stores.html'
    fields = '__all__'
    success_url = '/stores/list-stores/'