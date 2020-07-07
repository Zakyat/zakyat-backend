from django.urls import path, include

from dashboard.projs.views import index, СampaignListView, CampaignDetailView

app_name = 'projs'

urlpatterns = [
    path('campaigns/', СampaignListView.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),

]
