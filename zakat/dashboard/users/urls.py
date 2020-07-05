from django.urls import path, include
from .views import login, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
