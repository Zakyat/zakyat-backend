from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from accounts.models import Employee

# Create your views here.

class StaffListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'accounts.view_employee'
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'


class EmployeeCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'accounts.add_employee'
    model = Employee
    template_name = 'dashboard/employee/employee_create_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'


class EmployeeEdit(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'accounts.change_employee'
    model = Employee
    fields = '__all__'
    template_name = 'dashboard/employee/employee_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = get_object_or_404(Employee, pk=self.kwargs['pk'])
        return context


class EmployeeDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    permission_required = 'accounts.delete_employee'
    model = Employee
    success_url = reverse_lazy('dashboard:employee:staff_list')
    template_name = 'dashboard/employee/employee_delete_confirm.html'
