from django.urls import path, include
from .views import *

app_name = 'partner'

urlpatterns = [
    path('', PartnerList.as_view(), name="partners_list"),
    path('create/', PartnerCreate.as_view(), name="partner_create"),
    path('<int:pk>/', PartnerDetail.as_view(), name="partner_detail"),
    path('<int:pk>/delete/', PartnerDelete.as_view(), name="partner_delete"),
    path('<int:pk>/update/', PartnerUpdate.as_view(), name="partner_update"),
]
