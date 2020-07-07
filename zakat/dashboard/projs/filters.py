import django_filters
from django.db.models import Q

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

    # TODO add all fields (payment_opt, date??)
    @staticmethod
    def make_search1(value):
        return Q(title__icontains=value) \
               | Q(description__icontains=value) \
               | Q(created_by__user__username__icontains=value) \
               | Q(created_by__user__first_name__icontains=value) \
               | Q(created_by__user__last_name__icontains=value) \
               | Q(request__description__icontains=value) \
               | Q(closing_reason__icontains=value)

    @staticmethod
    def make_search2(value):
        return Q(request__user__user__last_name__icontains=value) \
               | Q(request__user__user__first_name__icontains=value) \
               | Q(request__user__user__username__icontains=value) \
               | Q(request__title__icontains=value)

    def filter_search(self, queryset, name, value):
        # TODO solve problem with searching through request's fields
        # queryset1 = queryset.filter(CampaignFilter.make_search1(value))
        # queryset2 = queryset.filter(CampaignFilter.make_search2(value))
        # queryset = queryset1.union(queryset2)

        queryset1 = list(queryset.filter(CampaignFilter.make_search1(value)).values_list('id', flat=True))
        queryset2 = list(queryset.filter(CampaignFilter.make_search2(value)).values_list('id', flat=True))
        qs = list(set(queryset1 + queryset2))
        queryset = queryset.filter(id__in=qs)
        return queryset
