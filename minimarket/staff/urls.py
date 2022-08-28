from django.urls import path

from staff.views import New_employee, List_staff, Delete_staff, Detail_staff, Update_staff

urlpatterns = [
    path('new-employee/', New_employee.as_view(), name='new_employee'),
    path('list-staff/', List_staff.as_view(), name='list_staff'),
    path('detail-staff/<int:pk>/', Detail_staff.as_view(), name='detail_staff'),
    path('delete-staff/<int:pk>/', Delete_staff.as_view(), name='delete_staff'),
    path('update-staff/<int:pk>/', Update_staff.as_view(), name='update_staff'),  
]