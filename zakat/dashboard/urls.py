from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.gatherings, name='gatherings'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
