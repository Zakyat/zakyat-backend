from django.urls import path, include

from dashboard.projs.views import index, C

app_name = 'projs'

urlpatterns = [
    # path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('c/', C.as_view(), name='c'),

]
