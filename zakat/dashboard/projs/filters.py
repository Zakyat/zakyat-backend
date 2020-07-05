import django_filters

from projects.models import Campaign


# TODO normalize view
class CampaignFilter(django_filters.FilterSet):
    STATUS_CHOICES = (
        ('all', 'All'),
        ('closed', 'Closed'),
        ('open', 'Open'),
    )
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES, field_name='Status', method='filter_status')

    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Campaign
        fields = ['search', 'status', ]

    def filter_status(self, queryset, name, value):
        # construct the full lookup expression.
        if value:
            if value == 'closed':
                queryset = queryset.filter(closed_at__isnull=False)
            elif value == 'open':
                queryset = queryset.filter(closed_at__isnull=True)
        return queryset

    def filter_search(self, queryset, name, value):
        # construct the full lookup expression.
        a=42
        return queryset