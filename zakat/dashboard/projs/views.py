from django.shortcuts import render
# Create your views here.
from django_filters.views import FilterView

from dashboard.projs.filters import CampaignFilter
from projects.models import Campaign


def index(request):
    return render(request, 'dashboard/projs/campaign_list.html', {'page_obj': Campaign.objects.all()})


# TODO pagination
class C(FilterView):
    template_name = 'dashboard/projs/campaign_list.html'
    filterset_class = CampaignFilter
    context_object_name = 'campaigns'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(C, self).get_context_data(object_list=object_list, **kwargs)
        context['count'] = len(object_list)
        return context

