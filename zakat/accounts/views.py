import operator
from functools import reduce

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views.generic.base import RedirectView

from . import models
from . import forms


class EmployeeRegistrationView(CreateView):
    form_class = forms.EmployeeRegistrationForm
    model = models.Employee
    template_name = 'employee_registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm
        context['employee_form'] = forms.EmployeeRegistrationForm
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)
        employee_form = forms.EmployeeRegistrationForm(request.POST)
        photo = request.FILES['photo']
        errors = {**user_form.errors, **employee_form.errors}
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.photo = photo
            employee.save()
            auth.login(request, user)
            return redirect('news:dashboard')
        else:
            return render(request, 'employee_registration.html', context={'errors': errors})


class EmployeeAuthorizationView(FormView):
    form_class = forms.EmployeeAuthorizationForm
    template_name = 'employee_authorization.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        employee = models.Employee.objects.get(user=user)
        if user is not None and employee is not None and employee.user.is_active:
            auth.login(request, employee.user)
            return redirect('news:dashboard')
        else:
            return render(request, 'employee_authorization.html', context={'error': 'Incorrect username or password'})


class EmployeeLogoutView(LoginRequiredMixin, RedirectView):
    url = 'accounts:employee_login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('accounts:employee_login')
