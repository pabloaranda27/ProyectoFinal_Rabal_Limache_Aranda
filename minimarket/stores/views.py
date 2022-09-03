from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from stores.models import Stores
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class List_stores(ListView):
    model= Stores
    template_name= 'stores/list_stores.html'

class New_store(AdminRequiredMixin, CreateView):
    model= Stores
    template_name= 'stores/new_store.html'
    fields = '__all__'
    success_url = '/stores/list-stores/'

class Detail_stores(DetailView):
    model= Stores
    template_name= 'stores/detail_stores.html'

class Delete_stores(AdminRequiredMixin, DeleteView):
    model= Stores
    template_name= 'stores/delete_stores.html'
    success_url = '/stores/list-stores/'

class Update_stores(AdminRequiredMixin, UpdateView):
    model= Stores
    template_name= 'stores/update_stores.html'
    fields = '__all__'
    success_url = '/stores/list-stores/'