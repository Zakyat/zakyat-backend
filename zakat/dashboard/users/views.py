from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
# TODO redirect to the 'Gatherings' page in the future
from django.urls import reverse_lazy

from .forms import LoginForm
from .helper import check_is_employee


# Create your views here.


@user_passes_test(lambda user: user.is_anonymous,
                  login_url=reverse_lazy('dashboard:projs:campaign-list'),
                  redirect_field_name=None)
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
