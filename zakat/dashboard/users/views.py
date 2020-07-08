from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from accounts.models import User
from .forms import SearchForm
from .helper import get_country_code
from django.db.models import Q
from payment.models import Transaction
# Create your views here.


# TODO redirect to the 'Gatherings' page in the future
# @user_passes_test(lambda user: user.is_anonymous,
#                   login_url='http://127.0.0.1:8000',
#                   redirect_field_name=None)
from .forms import LoginForm
from .helper import check_is_employee


def block_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == "POST":
        if user.isBlock:
            user.isBlock = False
        else:
            user.isBlock = True
        user.save()
        return redirect('dashboard:users:users_detail', pk)
    else:
        return render(request, 'dashboard/users/user_block_confirm.html', {'isBlock': user.isBlock})


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
    form_class = SearchForm
    paginate_by = 10
    template_name = 'dashboard/users/users_list.html'
    ordering = ['-user']

    def get_queryset(self):
        query = self.request.GET.get('q')
        display_paid_zakat = self.request.GET.get('zakat_persons')
        rubs = self.request.GET.get('zakat_sum_r')
        # dollars = self.request.GET.get('zakat_sum_d')
        country_code = get_country_code(query)
        if query:
            object_list = self.model.objects.filter(
                Q(user__username__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__email__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(citizenship__icontains=country_code) |
                Q(religion__icontains=query) |
                Q(birthdate__icontains=query) |
                Q(education__icontains=query) |
                Q(work__icontains=query) |
                Q(marital_status__icontains=query) |
                Q(address__icontains=query)
            )
        else:
            object_list = self.model.objects.all()
        if rubs:
            object_list = object_list.filter(transactions__amount__gt=rubs)
        return object_list


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
