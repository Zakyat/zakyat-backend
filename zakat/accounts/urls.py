from django.urls import path,include
from .views import *
from django.conf import settings


app_name = 'account'

urlpatterns = [
    path('', include('social_django.urls',namespace='social')),
    path('logout', user_logout,name='logout'),
    path('test',testView),
]