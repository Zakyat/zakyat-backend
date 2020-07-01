from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include
from .views import *
from dashboard.views import login
from .forms import PasswordResetForm

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
    path('logout/', logout, name='logout'),
    path('partners/', PartnerList.as_view(), name="partners_list"),
    path('partners/create/', PartnerCreate.as_view(), name="partner_create"),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name="partner_detail"),
    path('partners/<int:pk>/delete/', PartnerDelete.as_view(), name="partner_delete"),
    path('partners/<int:pk>/update/', PartnerUpdate.as_view(), name="partner_update"),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('password-reset/',
         PasswordResetView.as_view(template_name='dashboard/password_reset/password_reset.html',
                                   form_class=PasswordResetForm,
                                   success_url=reverse_lazy('dashboard:password_reset_done'),
                                   email_template_name='dashboard/password_reset/password_reset_email.html'
                                   ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='dashboard/password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(template_name='dashboard/password_reset/password_reset_confirm.html',
                                          success_url=reverse_lazy('dashboard:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='dashboard/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
