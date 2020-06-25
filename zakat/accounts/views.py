from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Employee
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import EmployeeCreateForm


# Create your views here.


class StaffListView(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'accounts/staff_list.html'


class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'accounts/employee_create_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'





class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'

class EmployeeDelete(DeleteView):
    model = Employee
    fields = '__all__'
