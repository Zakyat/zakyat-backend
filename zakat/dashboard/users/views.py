from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from accounts.models import User
from django.urls import reverse_lazy
# Create your views here.


# TODO redirect to the 'Gatherings' page in the future
# @user_passes_test(lambda user: user.is_anonymous,
#                   login_url='http://127.0.0.1:8000',
#                   redirect_field_name=None)
from .forms import LoginForm
from .helper import check_is_employee


def login(request):
    """Simple login page for employees only"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user is not None:
                if not check_is_employee(user):
                    messages.info(request, f'User {user.username} is not an employee!')
                else:
                    auth_login(request, user)
                    messages.info(request, 'Authenticated successfully!')
            else:
                messages.error(request, 'User credits are wrong!')
        else:
            messages.error(request, 'Given data is not valid!')
    else:
        form = LoginForm()

    return render(request, 'dashboard/users/login.html', {'form': form})


class UsersList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.view_user'
    model = User
    paginate_by = 10
    template_name = 'dashboard/users/users_list.html'
    ordering = ['-user']


class UserDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'users.view_user'
    model = User
    template_name = 'dashboard/users/user_detail.html'


class UserCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.create_user'
    template_name = 'dashboard/users/users_form.html'
    model = User
    fields = "__all__"


class UserDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'users.delete_user'
    model = User
    success_url = reverse_lazy('dashboard:users:users_list')
    template_name = 'dashboard/users/user_delete_confirm.html'


class UserUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = User
    fields = "__all__"
    template_name = 'dashboard/partner/partners_form.html'
