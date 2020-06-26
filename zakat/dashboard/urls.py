from django.urls import path, include
from .views import PartnerList, PartnerDetail, PartnerDelete, PartnerCreate, PartnerUpdate


from dashboard.views import login

app_name = 'dashboard'

urlpatterns = [
    # Here you write all your paths
    # For example 'staffs/', 'staffs/create'
    path('login/', login, name='login'),
    path('partners/', PartnerList.as_view(), name="partners_list"),
    path('partners/create/', PartnerCreate.as_view(), name="partner_create"),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name="partner_detail"),
    path('partners/<int:pk>/delete/', PartnerDelete.as_view(), name="partner_delete"),
    path('partners/<int:pk>/update/', PartnerUpdate.as_view(), name="partner_update"),
]
