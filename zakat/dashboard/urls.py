from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
from .forms import PasswordResetForm

app_name = 'dashboard'

urlpatterns = [
    path('', include('dashboard.users.urls')),
    path('', include('dashboard.projs.urls', namespace='projs')),
    #Here you write all your paths
    #For example 'staffs/', 'staffs/create'
    path('staffs/', include('dashboard.employee.urls', namespace='employee'),),
    path('partners/', include('dashboard.partner.urls', namespace='partner'),),
    # Here you write all your paths
    # For example 'staffs/', 'staffs/create'
    path('news/', include('dashboard.news_posts.urls', namespace='news_posts'),),
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
