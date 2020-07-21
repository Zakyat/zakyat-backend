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
