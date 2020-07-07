from django.urls import path, include

from dashboard.projs.views import index, СampaignListView, CampaignDetailView, close_campaign

app_name = 'projs'

urlpatterns = [
    path('campaigns/', СampaignListView.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaigns/<int:pk>/close/', close_campaign, name='campaign-close'),

]
