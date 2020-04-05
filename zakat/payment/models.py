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
