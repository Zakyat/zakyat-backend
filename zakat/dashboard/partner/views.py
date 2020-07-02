from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView
from partners.models import Partner


class PartnerList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'partners.view_partner'
    model = Partner
    paginate_by = 10
    template_name = 'dashboard/partner/partners_list.html'


class PartnerDetail(DetailView):
    permission_required = 'partners.view_partner'
    model = Partner
    template_name = 'dashboard/partner/partner_detail.html'


class PartnerCreate(CreateView):
    permission_required = 'partners.create_partner'
    template_name = 'dashboard/partner/partners_form.html'
    model = Partner
    fields = "__all__"


class PartnerDelete(DeleteView):
    permission_required = 'partners.delete_partner'
    model = Partner
    success_url = reverse_lazy('dashboard:partner:partners_list')


class PartnerUpdate(UpdateView):
    permission_required = 'partners.change_partner'
    model = Partner
    fields = "__all__"
    template_name = 'dashboard/partner/partners_form.html'
