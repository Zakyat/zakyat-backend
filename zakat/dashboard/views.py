from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render

from dashboard.forms import LoginForm


# Create your views here.


# TODO redirect to the correct view
# @user_passes_test(lambda user: user.is_anonymous,
#                   login_url='http://127.0.0.1:8000',
#                   redirect_field_name=None)
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)
                messages.info(request, 'Auth-ed successfully.')
            else:
                messages.error(request, 'User credits are wrong!')
    else:
        form = LoginForm()

    return render(request, 'dashboard/auth/login.html', {'form': form})
