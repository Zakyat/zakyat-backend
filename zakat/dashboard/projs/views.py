from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django_filters.views import FilterView

from dashboard.projs.filters import CampaignFilter
from dashboard.projs.forms import CloseCampaignForm
from projects.models import Campaign


def index(request):
    return render(request, 'dashboard/projs/campaign_list.html', {'page_obj': Campaign.objects.all()})


# TODO pagination
# TODO add access perms
class СampaignListView(FilterView):
    template_name = 'dashboard/projs/campaign_list.html'
    filterset_class = CampaignFilter
    context_object_name = 'campaigns'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(СampaignListView, self).get_context_data(object_list=object_list, **kwargs)
        context['count'] = len(object_list)
        return context


class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'dashboard/projs/campaign_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data(**kwargs)

        context['closing_form'] = CloseCampaignForm()
        return context


# TODO add access perms
@require_http_methods(["POST",])
def close_campaign(request, pk):
    try:
        campaign = Campaign.objects.get(id=pk)
    except Campaign.DoesNotExist as e:
        # TODO where to redirect
        raise e
    close_campaign_form = CloseCampaignForm(request.POST)
    # TODO show error messages
    if close_campaign_form.is_valid():
        cleaned_data = close_campaign_form.cleaned_data
        campaign.close_campaign(cleaned_data['text'])
    return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[pk,]))
