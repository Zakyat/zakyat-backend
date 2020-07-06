from django.urls import path, include
from .views import login, UsersList, UserDetail

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('', UsersList.as_view(), name="users_list"),
]
