from django.shortcuts import render
from partners.models import Partner
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class PartnerList(ListView):
    model = Partner
    paginate_by = 10
    template_name = 'dashboard/partners/partners_list.html'


class PartnerDetail(DetailView):
    model = Partner
    template_name = 'dashboard/partners/partner_detail.html'


class PartnerCreate(CreateView):
    template_name = 'dashboard/partners/partners_form.html'
    model = Partner
    fields = "__all__"


class PartnerDelete(DeleteView):
    model = Partner
    success_url = reverse_lazy('dashboard:partners_list')


class PartnerUpdate(UpdateView):
    model = Partner
    fields = "__all__"
    template_name = 'dashboard/partners/partners_form.html'
