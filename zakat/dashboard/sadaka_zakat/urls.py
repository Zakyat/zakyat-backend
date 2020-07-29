from django.urls import path
from .views import TransactionList

app_name = 'sadaka_zakat'

urlpatterns = [
    path('', TransactionList.as_view(), name='sadaka_zakat_list'),
]
