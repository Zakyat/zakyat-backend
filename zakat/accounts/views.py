from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from .models import User

# view for tepmplate auth testing
def testView(request):



    return render(request, 'test_auth.html')


def user_logout(request):
    logout(request)
    return render(request, 'test_auth.html')   # paste there you redirecting temolate
