from django.urls import path, include
from .views import *
from dashboard.views import login

app_name = 'employee'

urlpatterns = [
    path('', StaffListView.as_view(), name='staff_list'),
    path('create/', EmployeeCreate.as_view(), name='employee_create_form'),
    path('edit/<int:pk>/', EmployeeEdit.as_view(), name='employee_edit_form'),
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
]
