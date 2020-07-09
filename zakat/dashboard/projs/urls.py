from django.urls import path, include

from dashboard.projs.views import index, СampaignListView, CampaignDetailView, close_campaign, create_payment_option, \
    edit_campaign, create_campaign

app_name = 'projs'

urlpatterns = [
    path('campaigns/', СampaignListView.as_view(), name='campaign-list'),
    path('campaigns/create/', create_campaign, name='campaign-create'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaigns/<int:pk>/close/', close_campaign, name='campaign-close'),
    path('campaigns/<int:pk>/edit/', edit_campaign, name='campaign-edit'),
    path('campaigns/<int:campaign_pk>/create_payment_option/', create_payment_option, name='campaign-create-payment_option'),

]
