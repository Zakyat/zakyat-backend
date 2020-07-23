from django.urls import path, include
from .views import *

app_name = 'employee'

urlpatterns = [
    path('', StaffListView.as_view(), name='staff_list'),
    path('create_user/', user_creation_form, name='user_create_form'),
    path('create/', EmployeeCreate.as_view(), name='employee_create_form'),
    path('edit/<int:pk>/', EmployeeEdit.as_view(), name='employee_edit_form'),
    path('delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
    path('show_ui/', show_ui),
    path('example_form/', example_form),
]
