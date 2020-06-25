from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/staffs/', StaffListView.as_view(), name='staff_list'),

]
