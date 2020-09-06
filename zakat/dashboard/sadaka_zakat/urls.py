from django.urls import path
from .views import TransactionList, TransactionDetail, distribute


app_name = 'sadaka_zakat'

urlpatterns = [
    path('', TransactionList.as_view(), name='sadaka_zakat_list'),
    path('<int:pk>/', TransactionDetail.as_view(), name='sadaka_zakat_detail'),
    path('<int:pk>/distribute', distribute, name='distribute'),
]
