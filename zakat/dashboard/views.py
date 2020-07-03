from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView

from dashboard.forms import PostCreateForm, PostEditForm
from news.models import Post


class NewsList(LoginRequiredMixin, ListView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/news/news_list.html'
    paginate_by = 10
    ordering = 'created_at'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return redirect('dashboard:news_list')


class PostCreate(LoginRequiredMixin, CreateView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/news/post_create.html'
    success_url = reverse_lazy('dashboard:news_list')
    form_class = PostCreateForm


class PostEdit(LoginRequiredMixin, UpdateView):
    login_url = 'dashboard:login'
    model = Post
    form_class = PostEditForm
    template_name = 'dashboard/news/post_edit.html'
    success_url = reverse_lazy('dashboard:news_list')


class PostDetail(LoginRequiredMixin, DetailView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/news/post_detail.html'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return redirect('dashboard:news_list')

