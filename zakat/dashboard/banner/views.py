from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView
from .models import *

class BannersList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'banners.view_banner'
    model = Banner
    paginate_by = 10
    template_name = 'dashboard/banner/banners_list.html'

class BannerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'banners.view_banner'
    model = Banner
    template_name = 'dashboard/banner/banner_detail.html'


class BannerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'banners.create_banner'
    template_name = 'dashboard/banner/banners_form.html'
    model = Banner
    success_url = reverse_lazy('dashboard:banner:banners_list')
    fields = "__all__"


class BannerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'banners.delete_banner'
    model = Banner
    success_url = reverse_lazy('dashboard:banner:banners_list')
    template_name = 'dashboard/banner/banner_delete_confirm.html'


class BannerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'banners.change_banner'
    model = Banner
    success_url = reverse_lazy('dashboard:banner:banners_list')
    fields = "__all__"
    template_name = 'dashboard/banner/banners_form.html'