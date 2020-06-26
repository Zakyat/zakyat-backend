from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm
from django.contrib import messages


# Create your views here.


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
            return render(request, 'accounts/login.html', {'form': form})            
                # request.messages
                # return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
