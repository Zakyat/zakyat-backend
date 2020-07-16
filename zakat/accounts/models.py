from djongo import models
from django.contrib.auth.models import User as DjangoUser
from django.urls import reverse

from django_countries.fields import CountryField

# ---- Choice enums ----

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

DOCUMENT_TYPES = (
    ('pass_main', 'Passport main page'),
    ('pass_registration', 'Passport registration page'),
    ('birth', 'Birth certificate'),
    ('death', 'Death certificate'),
    ('marriage', 'Marriage certificate'),
    ('divorce', 'Divorce'),
    ('income', 'Income certificate'),
    ('unemployment', 'Unemployment office certificate'),
    ('medical', 'Disability/diagnosis'),
    ('study', 'Place of study'),
    ('loan', 'Loan'),
    ('rent', 'House book extract'),
    ('invoice', 'Invoice'),
)

RELATIONS = (
    ('father', 'Father'),
    ('mother', 'Mother'),
    ('son', 'Son'),
    ('daughter', 'Daughter'),
    ('brother', 'Brother'),
    ('sister', 'Sister'),
    ('other', 'Other'),
)


# ---- Models ----

class Work(models.Model):
    place = models.CharField(max_length=128)
    position = models.CharField(max_length=64)

    class Meta:
        abstract = True


class CashFlow(models.Model):
    type = models.CharField(choices=CASH_FLOW_TYPES, max_length=10)
    amount = models.IntegerField()
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='RUB')

    class Meta:
        abstract = True


class Document(models.Model):
    type = models.CharField(choices=DOCUMENT_TYPES, max_length=10)
    title = models.CharField(max_length=128)
    file = models.FileField(upload_to='uploads/')

    class Meta:
        abstract = True


class FamilyMember(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    relation = models.CharField(max_length=16, choices=RELATIONS)
    identification = models.EmbeddedField(model_container=Document)

    class Meta:
        abstract = True


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    citizenship = CountryField()
    religion = models.CharField(max_length=10, choices=RELIGIONS)
    birthdate = models.DateField()
    education = models.CharField(max_length=128)  # TODO: Why??
    work = models.EmbeddedField(model_container=Work, blank=True)
    marital_status =  models.CharField(max_length=10, choices=MARITAL_STATUS)
    address = models.CharField(max_length=128)
    isBlock = models.BooleanField(default=False)
    cash_flow = models.ArrayField(model_container=CashFlow, default=[])
    related_documents = models.ArrayField(model_container=Document, default=[])
    contact_person = models.EmbeddedField(model_container=FamilyMember)
    family_members = models.ArrayField(model_container=FamilyMember, default=[]) # ArrayField with nested FileField causes a problem
    # contact_person = models.EmbeddedField(model_container=FamilyMember)
    # family_members = models.ArrayField(model_container=FamilyMember,
    #                                    default=[])  # ArrayField with nested FileField causes a problem

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.work.place == '' or self.work.position == '':
            work = Work(position='Unemployed', place='Nowhere')
            self.work = work

        super(User, self).save(force_insert=force_insert,
                               force_update=force_update,
                               using=using,
                               update_fields=update_fields)


    def get_absolute_url(self):
        return reverse('dashboard:users:users_detail', args=[self.id])

class Employee(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='uploads', default='uploads/anon.png')
    bio = models.TextField()
    position = models.CharField(max_length=32)
    updated_at = models.DateTimeField(auto_now=True)
