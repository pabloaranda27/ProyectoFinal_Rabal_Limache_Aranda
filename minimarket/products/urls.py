from django.urls import path

from products.views import new_product, list_products, search_products, detail_product, update_product, delete_product, new_category, list_categories

urlpatterns = [
    path('new-product/', new_product, name='new_product'),
    path('new-category/', new_category, name='new_category'),
    path('list-products/', list_products, name='list_products'),
    path('list-categories/', list_categories, name='list_categories'),
    path('search-products/', search_products, name='search_products'),
    path('detail-product/<int:pk>/', detail_product, name='detail_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
]