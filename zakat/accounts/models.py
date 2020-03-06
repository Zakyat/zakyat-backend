from djongo import models
from django.contrib.auth.models import User as DjangoUser

from django_countries.fields import CountryField


MARITAL_STATUS = (
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("single", "Single"),
    ("widowed", "Widowed"),
    ("other", "Other"),
)

RELIGIONS = (
    ("muslim", "Muslim"),
    ("christian", "Christian"),
    ("jew", "Jewish"),
    ("atheist", "Atheist"),
    ("other", "Others"),
)

class Work(models.Model):
    place = models.CharField(max_length=128)
    position = models.CharField(max_length=64)

    class Meta:
        abstract = True

CASH_FLOW_TYPES = (
    ('salary', 'salary'),
    ('pension', 'pension'),
    ('allowance', 'allowance'),
    ('alimony', 'alimony'),
    ('expense', 'expense'),
    ('other', 'other'),
)

CURRENCIES = (
    ('RUB', 'Russian Ruble'),
    ('USD', 'US. Dollar'),
)

class CashFlow(models.Model):
    type = models.CharField(choices=CASH_FLOW_TYPES, max_length=10)
    amount = models.IntegerField()
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=CURRENCIES)

    class Meta:
        abstract = True


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    citizenship = CountryField()
    religion = models.CharField(max_length=10, choices=RELIGIONS)
    birthdate = models.DateField()
    education = models.CharField(max_length=128)    # TODO: Why??
    work = models.EmbeddedField(model_container=Work)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    address = models.CharField(max_length=128)
    cash_flow = models.ArrayField(model_container=CashFlow, default=[])
