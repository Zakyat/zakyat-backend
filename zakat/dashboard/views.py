from accounts.models import Employee
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
# class CustomMixin(object):
#
#     def get_context_data(self, **kwargs):
#         # Call class's get_context_data method to retrieve context
#         context = super().get_context_data(**kwargs)
#
#         context['page_title'] = 'My page title'
#         return context


class StaffListView(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'dashboard/employee/employee_create_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'

class EmployeeEdit(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'dashboard/employee/employee_create_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))



class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('staff_list')
    fields = '__all__'
