from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from . import models
from . import mixins
from . import forms


class DashboardView(LoginRequiredMixin, mixins.EmployeePermissionMixin, ListView):
    model = models.Post
    template_name = 'dashboard.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['post_form'] = forms.PostCreationForm
        return context


class NewsView(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = 'news.html'
    paginate_by = 10
