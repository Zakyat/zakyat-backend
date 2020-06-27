from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from . import models


class NewsView(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = 'news.html'
    paginate_by = 10
    ordering = 'created_at'
