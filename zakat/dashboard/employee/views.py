from functools import reduce

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView, View, FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, reverse
from accounts.models import Employee
from .forms import EmployeeForm, UserForm, UserEditForm, UserRegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.contrib.auth.models import User
import operator


# Create your views here.

def show_ui(request):
    return render(request, 'dashboard/user-profile.html')


def example_form(request):
    user_form = UserForm()
    employee_form = EmployeeForm()
    return render(request, 'dashboard/employee/example_form.html',
                  {'user_form': user_form, 'employee_form': employee_form})


def change_password(request, id):
    user = get_object_or_404(User, id=id)
    employee = get_object_or_404(Employee, user=user)
    form = PasswordChangeForm(user)
    if request.POST:
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:employee:employee_edit_form'))
    return render(request, 'dashboard/employee/change_password.html', {'form':form, 'employee':employee})

class StaffListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'accounts.view_employee'
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'
    ordering = ['-created_at']

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        search_query = self.request.GET.get('search', '')
        sort =  self.request.GET.get('sort', '')

        if search_query:
            qset = (
                    Q(phone_number__icontains=search_query) |
                    Q(position__icontains=search_query) |
                    Q(bio__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(user__username__icontains=search_query) |
                    Q(user__id__icontains=search_query)
            )
            employee_list = Employee.objects.filter(qset)
        else:
            employee_list = self.get_queryset()

        if sort:
            if sort == 'new_created':
                employee_list = employee_list.order_by('-created_at')
            if sort == 'old_created':
                employee_list = employee_list.order_by('created_at')
            if sort == 'new_updated':
                employee_list = employee_list.order_by('-updated_at')
            if sort == 'old_updated':
                employee_list = employee_list.order_by('updated_at')

        context = self.get_context_data()
        context['employee_list'] = employee_list
        return self.render_to_response(context)


class EmployeeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'accounts.add_employee'
    model = Employee
    template_name = 'dashboard/employee/employee_create_form.html'
    success_url = 'dashboard/staffs/'
    fields = '__all__'
    user_form_class = UserForm
    employee_form_class = EmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm()
        context['create_password'] = True
        context['employee_form'] = EmployeeForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            user_form = UserForm(request.POST)
            employee_form = EmployeeForm(request.POST)
            if user_form.is_valid() and employee_form.is_valid():
                user = user_form.save()
                employee_form.save(user)
                return HttpResponseRedirect(reverse('dashboard:employee:staff_list'))
            else:
                return render(request, 'dashboard/employee/employee_create_form.html',
                              {'user_form': user_form, 'employee_form': employee_form})


class EmployeeEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'accounts.change_employee'
    model = Employee
    fields = '__all__'
    template_name = 'dashboard/employee/employee_edit_form.html'
    success_url = '/dashboard/staffs/'  # HttpResponseRedirect(reverse('staff_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.employee = get_object_or_404(Employee, pk=self.kwargs['pk'])
        self.user = self.employee.user
        user_form = UserEditForm(instance=self.user)
        user_form.fields['user_id'].initial = self.user.id
        # user_form.user_id = self.kwargs['pk']
        print('self.user.id', self.user.id)
        context['employee'] = self.employee
        context['user_form'] = user_form
        context['employee_form'] = EmployeeForm(instance=self.employee)
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            user_form = UserEditForm(request.POST)
            employee_form = EmployeeForm(request.POST)
            if user_form.is_valid() and employee_form.is_valid():
                user = user_form.save()
                employee_form.save(user, edit=True)
                return HttpResponseRedirect(reverse('dashboard:employee:staff_list'))
            else:
                employee = get_object_or_404(Employee, pk=self.kwargs['pk'])
                return render(request, 'dashboard/employee/employee_edit_form.html',
                              {'user_form': user_form, 'employee_form': employee_form, 'employee': employee})


class EmployeeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'accounts.delete_employee'
    model = Employee
    success_url = reverse_lazy('dashboard:employee:staff_list')
    template_name = 'dashboard/employee/employee_delete_confirm.html'
