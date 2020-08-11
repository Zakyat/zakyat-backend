from django.core.validators import MinValueValidator
from djongo import models
from accounts.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from projects.models import Campaign
from django.contrib.auth.models import User as DjangoUser

from accounts.models import CURRENCIES
from projects.models import Campaign

PAYMENT_TYPES = (
    ('card', 'Card'),
    ('cash', 'Cash'),
    ('other', 'Some Other')
)

TRANSACTION_TYPES = (
    ('0', 'sadaka'),
    ('1', 'zakat'),
    ('2', 'direct')
)

# ---- Field enums ----
MONEY_TYPES = {
    True: 'Card',
    False: 'Cash Money',
    None: 'Some Other',
}

SUBSCRIPTION_DAYS = (
    (0, 'null'),
    (1, 'everyday'),
    (30, 'everymonth')
)

# DONATION_STATUS = (
#     ('in_progressing', 'in_processing'),
#     ('distribution', 'in_the_process_of_distribution'),
#     ('mny_in_th_gthr', 'money_in_the_gathering'),
#     ('in_th_process_of_trnsf_mny', 'in_the_process_of_transferring_money'),
#     ('mny_trnsf', 'money_transferred'),
# )


# ---- Models ----


def send_transaction_notification():
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'notification',
        {
            'type': 'notify',
            'transaction': Transaction.objects.filter(campaign=None).count()
        })


class Transaction(models.Model):
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='transactions', null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='transactions', blank=True,
                                 null=True)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES, default=0)
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='RUB')
    subscription_days = models.IntegerField(choices=SUBSCRIPTION_DAYS, default="0")
    type = models.CharField(max_length=16, choices=PAYMENT_TYPES, default=True)
    create_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Transaction, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        send_transaction_notification()

    def delete(self, using=None, keep_parents=False):
        super(Transaction, self).delete(using=None, keep_parents=False)
        send_transaction_notification()


class PaymentOptions(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='payment_options')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    # True means payment was made through credit card, False - with cash money, null - by other way
    payment_type = models.BooleanField(null=True, blank=True,
                                       help_text="Yes means payment was made through credit card, No - with cash money, Unknown - by other way")

    def get_payment_type(self):
        return MONEY_TYPES.get(self.payment_type)


class CardPaymentInfo(models.Model):
    payment_option = models.ForeignKey(PaymentOptions, on_delete=models.CASCADE, related_name='card_payment_infos')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='card_payment_infos')
    payer = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='card_payment_infos', null=False)
    rrn = models.CharField(max_length=20, unique=True)


class CashPaymentInfo(models.Model):
    payment_option = models.ForeignKey(PaymentOptions, on_delete=models.CASCADE, related_name='cash_payment_infos')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='cash_payment_infos')
    payer = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='cash_payment_infos', null=True)
    payer_name = models.CharField(max_length=30)


# class CampaignTransaction(models.Model):
#     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='camping_transaction')
#     transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='camping_transaction')
#     status = models.CharField(max_length=40, choices=DONATION_STATUS)
