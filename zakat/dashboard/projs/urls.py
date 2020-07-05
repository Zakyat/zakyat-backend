from django.urls import path, include

from dashboard.projs.views import index, СampaignListView

app_name = 'projs'

urlpatterns = [
    path('campaigns/', СampaignListView.as_view(), name='campaign-list'),

]
