from django.urls import path, include
from .views import *
from dashboard.views import login

app_name = 'dashboard'

urlpatterns = [
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('staffs/', StaffListView.as_view(), name='staff_list'),
    path('staffs/create/', EmployeeCreate.as_view(), name='employee_create_form'),
    path('staffs/edit/<int:pk>/', EmployeeEdit.as_view(), name='employee_edit_form'),
    path('staffs/delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
    # Here you write all your paths
    # For example 'staffs/', 'staffs/create'
    path('login/', login, name='login'),
    path('partners/', PartnerList.as_view(), name="partners_list"),
    path('partners/create/', PartnerCreate.as_view(), name="partner_create"),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name="partner_detail"),
    path('partners/<int:pk>/delete/', PartnerDelete.as_view(), name="partner_delete"),
    path('partners/<int:pk>/update/', PartnerUpdate.as_view(), name="partner_update"),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
]
