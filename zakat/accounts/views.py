from django.shortcuts import render
from django.contrib.auth import logout, authenticate


def testView(request):
    # if(request.user.is_authenticated):

    return render(request, 'test_auth.html')


def user_logout(request):
    logout(request)
    return render(request, 'test_auth.html')
