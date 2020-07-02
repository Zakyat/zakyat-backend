import django_filters

from projects.models import Campaign


class CampaignFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Campaign
        fields = ['title', 'description', ]