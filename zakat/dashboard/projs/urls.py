from django.urls import path, include

from dashboard.projs.views import index, C

app_name = 'projs'

urlpatterns = [
    # TODO change url path
    path('c/', C.as_view(), name='c'),

]
