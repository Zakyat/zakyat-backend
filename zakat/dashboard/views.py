from accounts.models import Employee
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.

class StaffListView(ListView):
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'


class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'dashboard/employee/employee_create_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'

class EmployeeDelete(DeleteView):
    model = Employee
    fields = '__all__'
