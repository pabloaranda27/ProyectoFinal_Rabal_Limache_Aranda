from django.contrib import admin
from django.urls import path, include

from minimarket.views import home, base, about

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('working-page/', base, name='base'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('staff/', include('staff.urls')),
    path('stores/', include('stores.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
