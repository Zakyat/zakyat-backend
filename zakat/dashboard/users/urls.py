from django.urls import path
from .views import login, logout, UsersList, UserDetail, UserCreate, UserUpdate, UserDelete, block_user

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('', UsersList.as_view(), name="users_list"),
    path('create/', UserCreate.as_view(), name="user_create"),
    path('<int:pk>/', UserDetail.as_view(), name="users_detail"),
    path('<int:pk>/delete/', UserDelete.as_view(), name="user_delete"),
    path('<int:pk>/update/', UserUpdate.as_view(), name="user_update"),
    path('<int:pk>/block/', block_user, name="user_block"),
    path('<int:pk>/unblock/', block_user, name="user_unblock"),
    path('logout/', logout, name='logout'),
]
