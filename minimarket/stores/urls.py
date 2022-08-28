from django.urls import path

from stores.views import New_store, List_stores, Detail_stores, Delete_stores, Update_stores

urlpatterns = [
    path('new-store/', New_store.as_view(), name='new_store'),
    path('list-stores/', List_stores.as_view(), name='list_stores'),
    path('detail-stores/<int:pk>/', Detail_stores.as_view(), name='detail_stores'),
    path('delete-stores/<int:pk>/', Delete_stores.as_view(), name='delete_stores'),
    path('update-stores/<int:pk>/', Update_stores.as_view(), name='update_stores'),  
]