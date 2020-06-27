from django import http
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from dashboard.auth_hepler import check_is_employee
from dashboard.forms import LoginForm
from partners.models import Partner
from accounts.models import Employee
from news.models import Post


class StaffListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'accounts.view_employee'
    model = Employee
    paginate_by = 20
    template_name = 'dashboard/employee/staff_list.html'


class EmployeeCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'accounts.add_employee'
    model = Employee
    template_name = 'dashboard/employee/employee_create_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))
    fields = '__all__'


class EmployeeEdit(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'accounts.change_employee'
    model = Employee
    fields = '__all__'
    template_name = 'dashboard/employee/employee_edit_form.html'
    success_url = '/dashboard/staffs/' #HttpResponseRedirect(reverse('staff_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = get_object_or_404(Employee, pk=self.kwargs['pk'])
        return context


class EmployeeDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    permission_required = 'accounts.delete_employee'
    model = Employee
    success_url = reverse_lazy('dashboard:staff_list')
    template_name = 'dashboard/employee/employee_delete_confirm.html'

# Create your views here.


# TODO redirect to the 'Gatherings' page in the future
# @user_passes_test(lambda user: user.is_anonymous,
#                   login_url='http://127.0.0.1:8000',
#                   redirect_field_name=None)
def login(request):
    """Simple login page for employees only"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user is not None:
                if not check_is_employee(user):
                    messages.info(request, f'User {user.username} is not an employee!')
                else:
                    auth_login(request, user)
                    messages.info(request, 'Authenticated successfully!')
            else:
                messages.error(request, 'User credits are wrong!')
        else:
            messages.error(request, 'Given data is not valid!')
    else:
        form = LoginForm()

    return render(request, 'dashboard/auth/login.html', {'form': form})


class PartnerList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'partners.view_partner'
    model = Partner
    paginate_by = 10
    template_name = 'dashboard/partners/partners_list.html'


class PartnerDetail(DetailView):
    permission_required = 'partners.view_partner'
    model = Partner
    template_name = 'dashboard/partners/partner_detail.html'


class PartnerCreate(CreateView):
    permission_required = 'partners.create_partner'
    template_name = 'dashboard/partners/partners_form.html'
    model = Partner
    fields = "__all__"


class PartnerDelete(DeleteView):
    permission_required = 'partners.delete_partner'
    model = Partner
    success_url = reverse_lazy('dashboard:partners_list')


class PartnerUpdate(UpdateView):
    permission_required = 'partners.change_partner'
    model = Partner
    fields = "__all__"
    template_name = 'dashboard/partners/partners_form.html'


class NewsList(LoginRequiredMixin, ListView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/news/news_list.html'
    paginate_by = 10
    ordering = 'created_at'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return http.HttpResponse(status=200)


class PostCreate(LoginRequiredMixin, CreateView):
    login_url = 'dashboard:login'
    model = Post
    fields = '__all__'
    template_name = 'dashboard/news/post_create.html'
    success_url = 'dashboard:news_list'


class PostEdit(LoginRequiredMixin, UpdateView):
    login_url = 'dashboard:login'
    model = Post
    fields = ('title', 'description', 'project',)
    template_name = 'dashboard/news/post_edit.html'
    success_url = 'dashboard:news_list'


class PostDetail(LoginRequiredMixin, DetailView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/news/post_detail.html'

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        Post.objects.get(id=post_id).delete()
        return redirect('dashboard:news_list')

