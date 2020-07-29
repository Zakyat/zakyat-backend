from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from .models import User


def testView(request):
    # if(request.user.is_authenticated):
    #
    #     djuser = request.user
    #     # if(User.objects.get(user=djuser)):
    #
    #     zakyatUser = User.objects.create(user=djuser)
    #     zakyatUser.save()

    return render(request, 'test_auth.html')


def user_logout(request):
    logout(request)
    return render(request, 'test_auth.html')
