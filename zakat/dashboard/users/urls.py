from django.urls import path, include
from .views import login, UsersList, UserDetail, UserCreate, UserUpdate, UserDelete

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('', UsersList.as_view(), name="users_list"),
    path('create/', UserCreate.as_view(), name="user_create"),
    path('<int:pk>/', UserDetail.as_view(), name="users_detail"),
    path('<int:pk>/delete/', UserDelete.as_view(), name="user_delete"),
    path('<int:pk>/update/', UserUpdate.as_view(), name="user_update"),
]
