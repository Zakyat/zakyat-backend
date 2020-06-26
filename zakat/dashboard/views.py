from accounts.models import Employee
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class StaffListView(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'dashboard/employee/employee_create_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'

class EmployeeEdit(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'dashboard/employee/employee_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = get_object_or_404(Employee, pk=self.kwargs['pk'])
        return context

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('dashboard:staff_list')
    template_name = 'dashboard/employee/employee_delete_confirm.html'

