import os
from datetime import datetime

from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import ValidationError
from django.urls import reverse
from django_countries.fields import CountryField
# from djongo import models

from django.db import models

# ---- Choice enums ----
from zakat.settings import BASE_DIR

MARITAL_STATUS = (
    ('-', '----'),
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("single", "Single"),
    ("widowed", "Widowed"),
    ("other", "Other"),
)

RELIGIONS = (
    ('-', '----'),
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

EMPTY_FIELDS_LIST = [
    'religion',
    'birthdate',
    'education',
    'marital_status',
    'address',
]


def set_default_work():
    work = Work(position='Unemployed', place='Nowhere')
    return work.id


# ---- Models ----

class Work(models.Model):
    place = models.CharField(max_length=128)
    position = models.CharField(max_length=64)

    # class Meta:
    #     abstract = True


class CashFlow(models.Model):
    type = models.CharField(choices=CASH_FLOW_TYPES, max_length=10)
    amount = models.IntegerField()
    description = models.TextField()
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='RUB')

    # class Meta:
    #     abstract = True


class Document(models.Model):
    type = models.CharField(choices=DOCUMENT_TYPES, max_length=10, blank=True)
    title = models.CharField(max_length=128, blank=True)
    # file = models.FileField(upload_to='media/uploads')
    file = models.FilePathField(path=os.path.join(BASE_DIR, 'media'), recursive=True, blank=True)

    # class Meta:
    #     abstract = True


class FamilyMember(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    relation = models.CharField(max_length=16, choices=RELATIONS)
    # identification = models.EmbeddedField(model_container=Document)
    identification = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     abstract = True


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16, blank=True)
    citizenship = CountryField(default='RU')
    religion = models.CharField(max_length=10, choices=RELIGIONS, default='-')
    birthdate = models.DateField(blank=True, default=datetime.strptime('1000-12-12', '%Y-%m-%d'))
    education = models.CharField(max_length=128, default='-')  # TODO: Why??
    # work = models.EmbeddedField(model_container=Work, blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, default=set_default_work(), blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS, default='-')
    address = models.CharField(max_length=128, default='-')
    isBlock = models.BooleanField(default=False)
    gender = models.BooleanField(null=True, help_text='Yes means Male, No means Female')

    # cash_flow = models.ArrayField(model_container=CashFlow, default=[])
    # related_documents = models.ArrayField(model_container=Document, blank=True, default=[])



    # contact_person = models.EmbeddedField(model_container=FamilyMember)
    # family_members = models.ArrayField(model_container=FamilyMember, default=[]) # ArrayField with nested FileField causes a problem
    # contact_person = models.EmbeddedField(model_container=FamilyMember)
    # family_members = models.ArrayField(model_container=FamilyMember,
    #                                    default=[])  # ArrayField with nested FileField causes a problem

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #
    #     # self.set_default_work()
    #     # if self.work is None:
    #     #     work = Work(position='Unemployed', place='Nowhere')
    #     #     self.work = work
    #
    #     super(User, self).save(force_insert=force_insert,
    #                            force_update=force_update,
    #                            using=using,
    #                            update_fields=update_fields)

    def clean(self):
        if not self.check_for_empty_fields():
            raise ValidationError('Not all fields are filled!')

    def get_absolute_url(self):
        return reverse('dashboard:users:users_detail', args=[self.id])

    def check_for_empty_fields(self):
        default_date = datetime.strptime('1000-12-12', '%Y-%m-%d').date()
        counter = 0
        for field in self.EMPTY_FIELDS_LIST:
            value = self.__getattribute__(field)

            if field == 'birthdate':
                if default_date != value:
                    counter += 1
            elif value != '-':
                counter += 1

            # elif value is not None and field not in ['birthdate', 'marital_status', 'religion']:
            #     counter += 1
        return counter == 0 or counter == len(self.EMPTY_FIELDS_LIST)


class Employee(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='uploads', default='uploads/anon.png')
    bio = models.TextField()
    position = models.CharField(max_length=32)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
