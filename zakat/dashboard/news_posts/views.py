from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.list import ListView

from dashboard.news_posts.forms import PostCreateForm, PostEditForm
from dashboard.news_posts.mixins import EmployeePermissionMixin
from news.models import Post
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect



class NewsListView(LoginRequiredMixin, EmployeePermissionMixin, ListView):
    login_url = 'dashboard:users:login'
    model = Post
    paginate_by = 20
    template_name = 'dashboard/news/news.html'
    ordering = ['-created_at']

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        search_query = self.request.GET.get('search', '')

        if search_query:
            query_set = (
                    Q(title__icontains=search_query) |
                    Q(project__title__icontains=search_query)
            )
            news_list = Post.objects.filter(query_set)
        else:
            news_list = self.get_queryset()

        context = self.get_context_data()
        context['news_list'] = news_list
        return self.render_to_response(context)

class NewsEditView(LoginRequiredMixin, EmployeePermissionMixin, UpdateView):
    login_url = 'dashboard:users:login'
    model = Post
    form_class = PostEditForm
    template_name = 'dashboard/news/news_edit.html'

class NewsCreateView(LoginRequiredMixin, EmployeePermissionMixin, CreateView):
    login_url = 'dashboard:users:login'
    model = Post
    template_name = 'dashboard/news/news_create.html'
    success_url = 'dashboard/news/newz'
    fields = '__all__'
    news_form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_form'] = PostCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            news_create_form = PostCreateForm(request.POST)
            if news_create_form.is_valid():
                news_created = news_create_form.save(commit=False)
                news_created.created_by = request.user.employee
                news_created.save()
                return HttpResponseRedirect(reverse('dashboard:news_posts:newz'))
            else:
                return render(request, 'dashboard/news/news_create.html', {'news_create_form': news_create_form, 'form': news_create_form})


class NewsList(LoginRequiredMixin, EmployeePermissionMixin, ListView):
    login_url = 'dashboard:users:login'
    model = Post
    template_name = 'dashboard/news/news_list.html'
    paginate_by = 10
    ordering = 'created_at'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return redirect('dashboard:news_posts:news_list')


class PostCreate(LoginRequiredMixin, EmployeePermissionMixin, CreateView):
    login_url = 'dashboard:users:login'
    model = Post
    template_name = 'dashboard/news/post_create.html'
    success_url = reverse_lazy('dashboard:news_posts:news_list')
    form_class = PostCreateForm


class PostEdit(LoginRequiredMixin, EmployeePermissionMixin, UpdateView):
    login_url = 'dashboard:users:login'
    model = Post
    form_class = PostEditForm
    template_name = 'dashboard/news/post_edit.html'
    success_url = reverse_lazy('dashboard:news_posts:news_list')


class PostDetail(LoginRequiredMixin, EmployeePermissionMixin, DetailView):
    login_url = 'dashboard:users:login'
    model = Post
    template_name = 'dashboard/news/post_detail.html'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return redirect('dashboard:news_posts:news_list')
