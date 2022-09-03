from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from staff.models import Staff
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class List_staff(AdminRequiredMixin, ListView):
        model= Staff
        template_name= 'staff/list_staff.html'
        
class New_employee(AdminRequiredMixin, CreateView):
    model= Staff
    template_name= 'staff/new_employee.html'
    fields = '__all__'
    success_url = '/staff/list-staff/'

class Detail_staff(AdminRequiredMixin, DetailView):
    model= Staff
    template_name= 'staff/detail_staff.html'

class Delete_staff(AdminRequiredMixin, DeleteView):
    model= Staff
    template_name= 'staff/delete_staff.html'
    success_url = '/staff/list-staff/'

class Update_staff(AdminRequiredMixin, UpdateView):
    model= Staff
    template_name= 'staff/update_staff.html'
    fields = '__all__'
    success_url = '/staff/list-staff/'