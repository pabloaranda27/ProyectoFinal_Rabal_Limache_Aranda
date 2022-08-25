from django.urls import path

from staff.views import New_employee, List_staff

urlpatterns = [
    path('new-employee/', New_employee.as_view(), name='new_employee'),
    path('list-staff/', List_staff.as_view(), name='list_staff'),
]