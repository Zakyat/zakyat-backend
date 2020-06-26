from django.urls import path, include
from .views import PartnerList, PartnerDetail


app_name = 'dashboard'

app_name = 'dashboard'

urlpatterns = [
    path('partners/', PartnerList.as_view(), name="partners_list"),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name="partner_detail")
]
