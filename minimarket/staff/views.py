from django.views.generic import CreateView, ListView

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