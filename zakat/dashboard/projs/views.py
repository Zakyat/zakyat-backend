from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django_filters.views import FilterView

from dashboard.projs.filters import CampaignFilter
from dashboard.projs.forms import CloseCampaignForm, PaymentOptionsForm, CampaignForm
from payment.models import PaymentOptions
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
        context['payment_option_form'] = PaymentOptionsForm()
        context['payment_options'] = self.object.get_payment_options()

        return context


# TODO add access perms
@require_http_methods(["POST", ])
def close_campaign(request, pk):
    try:
        campaign = Campaign.objects.get(id=pk)
    except Campaign.DoesNotExist as e:
        raise e
    close_campaign_form = CloseCampaignForm(request.POST)
    if close_campaign_form.is_valid():
        cleaned_data = close_campaign_form.cleaned_data
        campaign.close_campaign(cleaned_data['text'])
    return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[pk, ]))


# TODO add access perms
@require_http_methods(["POST", ])
def payment_option_create(request, campaign_pk):
    try:
        campaign = Campaign.objects.get(id=campaign_pk)
    except Campaign.DoesNotExist as e:
        raise e
    payment_option_create_form = PaymentOptionsForm(request.POST)
    if payment_option_create_form.is_valid():
        cleaned_data = payment_option_create_form.cleaned_data
        payment_option = PaymentOptions(**cleaned_data)
        campaign.payment_option_create(payment_option)
    return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[campaign_pk, ]))


def campaign_edit(request, pk):
    try:
        campaign = Campaign.objects.get(id=pk)
    except Campaign.DoesNotExist as e:
        raise e
    status_code = 200
    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            campaign = form.save()
            return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[campaign.id]))
        else:
            status_code = 400
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'dashboard/projs/campaign_edit.html', {'form': form, 'campaign_id': campaign.id},
                  status=status_code)


def campaign_create(request):
    status_code = 200
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user.employee
            campaign.save()
            return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[campaign.id]))
        else:
            status_code = 400
    else:
        form = CampaignForm()
    return render(request, 'dashboard/projs/campaign_create.html', {'form': form}, status=status_code)


def payment_option_edit(request, pk):
    try:
        payment_option = PaymentOptions.objects.get(pk=pk)
    except PaymentOptions.DoesNotExist as e:
        raise e
    status_code = 200
    if request.method == 'POST':
        form = PaymentOptionsForm(request.POST, instance=payment_option)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[payment_option.campaign.id]))
        else:
            status_code = 400
    else:
        form = PaymentOptionsForm(instance=payment_option)
    return render(request, 'dashboard/projs/payment_option_edit.html', {'form': form},
                  status=status_code)

@require_http_methods(["POST", ])
def payment_option_delete(request, pk):
    try:
        payment_option = PaymentOptions.objects.get(pk=pk)
        campaign_id = payment_option.campaign_id
        payment_option.delete()
        return redirect(reverse_lazy('dashboard:projs:campaign-detail', args=[campaign_id]))
    except PaymentOptions.DoesNotExist as e:
        raise e


@require_http_methods(["POST", ])
def campaign_delete(request, pk):
    try:
        Campaign.objects.get(pk=pk).delete()
        return redirect(reverse_lazy('dashboard:projs:campaign-list'))
    except Campaign.DoesNotExist as e:
        raise e
