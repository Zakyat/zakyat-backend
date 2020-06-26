from django.shortcuts import render
from partners.models import Partner
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PartnerList(ListView):
    model = Partner
    paginate_by = 10
    template_name = 'dashboard/partners/partners_list.html'


class PartnerDetail(DetailView):
    model = Partner
    template_name = 'dashboard/partners/partner_detail.html'
