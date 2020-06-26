from django.urls import path, include


app_name = 'dashboard'

urlpatterns = [
    path('partners/', include('dashboard.partners.urls')),
]
