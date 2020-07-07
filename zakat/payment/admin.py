from django.contrib import admin

# Register your models here.
from payment.models import PaymentOptions

admin.site.register(PaymentOptions)
