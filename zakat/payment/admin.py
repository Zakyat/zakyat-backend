from django.contrib import admin
from payment.models import Transaction, PaymentOptions

admin.site.register(Transaction)
admin.site.register(PaymentOptions)
