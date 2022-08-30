from django.urls import path

from products.views import new_product, list_products, search_products, detail_product, update_product, delete_product

urlpatterns = [
    path('new-product/', new_product, name='new_product'),
    path('list-products/', list_products, name='list_products'),
    path('search-products/', search_products, name='search_products'),
    path('detail-product/<int:pk>/', detail_product, name='detail_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
]