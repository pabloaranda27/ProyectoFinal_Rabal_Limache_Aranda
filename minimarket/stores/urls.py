from django.urls import path

from stores.views import New_store, List_stores

urlpatterns = [
    path('new-store/', New_store.as_view(), name='new_store'),
    path('list-stores/', List_stores.as_view(), name='list_stores'),
]