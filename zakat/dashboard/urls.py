from django.urls import path, include
from .views import *

app_name = 'dashboard'

urlpatterns = [
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('staffs/', StaffListView.as_view(), name='staff_list'),
    path('staffs/create', EmployeeCreate.as_view(), name='employee_create_form'),
]
