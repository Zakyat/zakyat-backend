from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'dashboard'

urlpatterns = [
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('logout/', LogoutView.as_view(), name='logout'),
]
