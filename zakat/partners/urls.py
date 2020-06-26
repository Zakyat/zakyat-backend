from django.urls import path
from .views import PartnerList, PartnerDetail

app_name = 'partners_dashboard'

urlpatterns = [
    path('', PartnerList.as_view(), name="partners_list"),
    path('<int:pk>/', PartnerDetail.as_view(), name="partner_detail")
]
