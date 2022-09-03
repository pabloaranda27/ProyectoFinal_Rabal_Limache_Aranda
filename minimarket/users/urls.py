from django.urls import path
from users.views import login_request, register, show_profile, update_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('show-profile/<str:username>/', show_profile, name='show_profile'),
    path('update-profile/<str:username>/', update_profile, name='update_profile'),
]