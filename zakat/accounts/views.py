from django.shortcuts import render
from .models import Employee
from django.views.generic.list import ListView


# Create your views here.


class StaffListView(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'accounts/staff_list.html'





