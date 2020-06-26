from django.urls import path, include

from dashboard.views import login

app_name = 'dashboard'

urlpatterns = [
    # Here you write all your paths
    # For example 'staffs/', 'staffs/create'

    path('login/', login, name='login'),
]
