from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, Sum
from django.views.generic.list import ListView

from payment.models import Transaction
from .forms import SearchForm


class TransactionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'transaction.view_transaction'
    model = Transaction
    form_class = SearchForm
    paginate_by = 10
    template_name = 'dashboard/sadaka_zakat/sadaka_zakat_list.html'
    # ordering = ['-transaction']

    # def __init__(self, **kwargs):
    #  super().__init__(**kwargs)
    #  self.zakat = False
    #
    # def get_queryset(self):
    #  query = self.request.GET.get('q')
    #  rubs = self.request.GET.get('zakat_sum_r')
    #  zakat = self.request.GET.get('zakat_persons')
    #  self.query = query
    #  self.rubs = rubs
    #  self.zakat = zakat
    #  country_code = get_country_code(query)
    #  if query:
    #   object_list = self.model.objects.filter(
    #    Q(user__username__icontains=query) |
    #    Q(user__first_name__icontains=query) |
    #    Q(user__last_name__icontains=query) |
    #    Q(user__email__icontains=query) |
    #    Q(phone_number__icontains=query) |
    #    Q(citizenship__icontains=country_code) |
    #    Q(religion__icontains=query) |
    #    Q(birthdate__icontains=query) |
    #    Q(education__icontains=query) |
    #    Q(work__icontains=query) |
    #    Q(marital_status__icontains=query) |
    #    Q(address__icontains=query)
    #   )
    #  else:
    #   object_list = self.model.objects.all()
    #  if self.zakat == 'paid':
    #   object_list = object_list.filter(transactions__transaction_type=1)  # 1 means zakat type
    #  elif self.zakat == 'not paid':
    #   trans = [t.user.id for t in Transaction.objects.filter(transaction_type=1)]
    #   object_list = object_list.exclude(id__in=trans)  # 1 means zakat type
    #  if self.rubs:
    #   object_list = list(object_list.annotate(total_sum=Sum('transactions__amount')).filter(total_sum__gte=rubs))
    #  # if self.zakat == 'not paid':
    #  #     object_list = object_list.exclude()
    #  return object_list
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #  context = super().get_context_data()
    #  context['zakat'] = self.zakat
    #  context['more_than_sum'] = self.rubs if self.rubs is not None else -1
    #  context['query'] = self.query
    #  return context
    #
