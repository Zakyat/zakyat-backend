from djongo import models
from django.contrib.auth.models import User as DjangoUser

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

class PaymentOptions(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='payment_options')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    # True means payment was made through credit card, False - with cash money, null - by other way
	# TODO change representatin fields in admin page
    payment_type = models.BooleanField(null=True, blank=True, help_text="Yes means payment was made through credit card, No - with cash money, Unknown - by other way")