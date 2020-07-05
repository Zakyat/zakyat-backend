from django.urls import path, include

from dashboard.projs.views import index, СampaignListView

app_name = 'projs'

urlpatterns = [
    # TODO change url path
    path('c/', СampaignListView.as_view(), name='c'),

]
