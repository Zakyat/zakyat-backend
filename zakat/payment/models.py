from django.core.validators import MinValueValidator
from djongo import models
from accounts.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from projects.models import Campaign

# ---- Field enums ----

PAYMENT_TYPES = (
    ('card', 'Card'),
    ('cash', 'Cash'),
    ('transfer', 'Transfer'),
    ('withdraw', 'Withdraw'),
)

TRANSACTION_TYPES = (
    ('0', 'sadaka'),
    ('1', 'zakat'),
    ('2', 'direct')
)


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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='transactions')
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='transactions', blank=True, null=True)
    type = models.CharField(max_length=16, choices=PAYMENT_TYPES)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES, default=0)
    description = models.TextField()

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
    # True means payment was made through credit card, False - with cash money, bull - by other way
    payment_type = models.BooleanField(null=True, blank=True)
