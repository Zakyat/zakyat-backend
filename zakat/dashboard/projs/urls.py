from django.urls import path, include

from dashboard.projs.views import CampaignListView, CampaignDetailView, close_campaign, payment_option_create, \
    campaign_edit, campaign_create, payment_option_edit, payment_option_delete, campaign_delete

app_name = 'projs'

urlpatterns = [
    path('campaigns/', CampaignListView.as_view(), name='campaign-list'),
    path('campaigns/create/', campaign_create, name='campaign-create'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaigns/<int:pk>/close/', close_campaign, name='campaign-close'),
    path('campaigns/<int:pk>/edit/', campaign_edit, name='campaign-edit'),
    path('campaigns/<int:pk>/delete/', campaign_delete, name='campaign-delete'),
    path('campaigns/<int:campaign_pk>/payment_options/create/', payment_option_create, name='campaign-create-payment_option'),
    path('campaigns/payment_options/<int:pk>/edit/', payment_option_edit, name='payment_option-edit'),
    path('campaigns/payment_options/<int:pk>/delete/', payment_option_delete, name='payment_option-delete'),

]
