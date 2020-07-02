from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *


app_name = 'dashboard'


urlpatterns = [
    path('gathering/', gatherings, name='gatherings'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('dashboard.users.urls')),
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('staffs/', include('dashboard.employee.urls', namespace='employee'),),
    path('partners/', include('dashboard.partner.urls', namespace='partner'),),
    # Here you write all your paths
    # For example 'staffs/', 'staffs/create'
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
]
