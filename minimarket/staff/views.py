from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.shortcuts import render
from staff.models import Staff

class List_staff(ListView):
    model= Staff
    template_name= 'staff/list_staff.html'

class New_employee(CreateView):
    model= Staff
    template_name= 'staff/new_employee.html'
    fields = '__all__'
    success_url = '/staff/list-staff/'

class Detail_staff(DetailView):
    model= Staff
    template_name= 'staff/detail_staff.html'

class Delete_staff(DeleteView):
    model= Staff
    template_name= 'staff/delete_staff.html'
    success_url = '/staff/list-staff/'

class Update_staff(UpdateView):
    model= Staff
    template_name= 'staff/update_staff.html'
    fields = '__all__'
    success_url = '/staff/list-staff/'