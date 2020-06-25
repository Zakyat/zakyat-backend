from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/staffs/', StaffListView.as_view(), name='staff_list'),
    path('dashboard/staffs/create', EmployeeCreate.as_view(), name='employee_create_form'),

]
