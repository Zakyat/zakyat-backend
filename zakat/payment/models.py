from djongo import models
from django.contrib.auth.models import User as DjangoUser

from projects.models import Campaign

# ---- Field enums ----

TRANSACTION_TYPES = (
	('card',     'Card'),
	('cash',     'Cash'),
	('transfer', 'Transfer'),
	('withdraw', 'Withdraw'),
)

SUBSCRIPTION_DAYS = (
        (None, 'Null'), 
        (1, 'everyday'), 
        (30, 'everymonth')
    )

DONATION_STATUS = (
        ('in_progressing', 'in_processing'),
        ('distribution', 'in_the_process_of_distribution'),
        ('mny_in_th_gthr', 'money_in_the_gathering'),
        ('in_th_process_of_trnsf_mny', 'in_the_process_of_transferring_money'),
        ('mny_trnsf', 'money_transferred'),
    )

TRANSACTION_TYPES = (
	('card',     'Card'),
	('cash',     'Cash'),
	('transfer', 'Transfer'),
	('withdraw', 'Withdraw'),
)

SUBSCRIPTION_DAYS = (
        (None, 'Null'), 
        (1, 'everyday'), 
        (30, 'everymonth')
    )

# ---- Models ----

class Transaction(models.Model):
	amount = models.IntegerField()
	currency = models.CharField(max_length=20)
	subscription_days = models.IntegerField(choices=SUBSCRIPTION_DAYS)
	user = models.ForeignKey(DjangoUser, on_delete=models.DO_NOTHING, related_name='transactions')
	campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='transactions')
	type = models.CharField(max_length=16, choices=TRANSACTION_TYPES)
	description = models.TextField()


class CardPaymentInfo(models.Model):
    payment_option = None
    payment = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='card_payment_infos')
    payer = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='card_payment_infos', null=False)
    rrn = models.CharField(max_length=20, unique=True)
    

class CashPaymentInfo(models.Model):
    payment_option = None
    payment = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='cash_payment_infos')
    payer = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='cash_payment_infos', null=True)
    payer_name = models.CharField(max_length=30)


class CampaignTransaction(models.Model):
    gathering = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='camping_transaction')
    payment = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='camping_transaction')
    status = models.CharField(max_length=40, choices=DONATION_STATUS)

