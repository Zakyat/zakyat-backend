from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django_filters.views import FilterView

from payment.models import Transaction
from .forms import SearchForm
from .helper import get_amount, get_transaction_type
from ..projs.filters import CampaignFilter


@method_decorator(staff_member_required, name='dispatch')
class TransactionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'transaction.view_transaction'
    model = Transaction
    form_class = SearchForm
    paginate_by = 10
    template_name = 'dashboard/sadaka_zakat/sadaka_zakat_list.html'
    ordering = ['create_at']

    def get_queryset(self):
        query = self.request.GET.get('q')
        transaction_type = self.request.GET.get('transaction_type')
        distribute = self.request.GET.get('distribute')
        self.query = query
        self.transaction_type = transaction_type
        self.distribute = distribute
        amount = get_amount(query)
        transaction_type = get_transaction_type(query)
        if query:
            object_list = self.model.objects.filter(
                Q(amount=amount) |
                Q(transaction_type=transaction_type) |
                Q(description__contains=query) |
                Q(user__user__username=query) |
                Q(campaign__title=query)
            )
        else:
            object_list = self.model.objects.all()
        if self.transaction_type == 'sadaka':
            object_list = object_list.filter(transaction_type='0')  # 0 -> sadaka
        elif self.transaction_type == 'direct sadaka':
            object_list = object_list.filter(transaction_type='2')  # 2 -> direct sadaka
        elif self.transaction_type == 'zakat':
            object_list = object_list.filter(transaction_type='1')  # 1 -> zakat
        if self.distribute == 'true':
            object_list = object_list.filter(campaign=None)
        elif self.distribute == 'false':
            object_list = object_list.exclude(campaign=None)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['type'] = self.transaction_type
        context['distribute'] = self.distribute if self.distribute is not None else 'false'
        context['query'] = self.query
        return context


@method_decorator(staff_member_required, name='dispatch')
class TransactionDetail(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = 'users.view_user'
    context_object_name = 'campaigns'
    template_name = 'dashboard/sadaka_zakat/sadaka_zakat_detail.html'
    filterset_class = CampaignFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TransactionDetail, self).get_context_data(object_list=object_list, **kwargs)
        context['count'] = len(object_list)
        context['transaction'] = Transaction.objects.get(id=self.kwargs['pk'])
        return context
