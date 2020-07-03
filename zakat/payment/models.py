from djongo import models
from django.contrib.auth.models import User as DjangoUser
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from projects.models import Campaign


TRANSACTION_TYPES = (
	('card',     'Card'),
	('cash',     'Cash'),
	('transfer', 'Transfer'),
	('withdraw', 'Withdraw'),
)


class Transaction(models.Model):
	amount = models.IntegerField()
	user = models.ForeignKey(DjangoUser, on_delete=models.DO_NOTHING, related_name='transactions')
	campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='transactions')
	type = models.CharField(max_length=16, choices=TRANSACTION_TYPES)
	description = models.TextField()

	def save(self, force_insert=False, force_update=False, using=None,
			 update_fields=None):
		super(Transaction, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

		layer = get_channel_layer()
		async_to_sync(layer.group_send)(
			'notification',
			{
				'type': 'notify',
				'transaction': Transaction.objects.count()
			})


class PaymentOptions(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='payment_options')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    # True means payment was made through credit card, False - with cash money, bull - by other way
    payment_type = models.BooleanField(null=True, blank=True)