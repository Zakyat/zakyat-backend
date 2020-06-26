from django.urls import path, include

urlpatterns = [
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('', include('dashboard.urls'))
]
