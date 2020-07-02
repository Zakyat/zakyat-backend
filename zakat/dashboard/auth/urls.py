from django.urls import path, include
from .views import login

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
]
