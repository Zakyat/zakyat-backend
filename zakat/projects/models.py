from django.utils.timezone import localtime
from djongo import models
from accounts.models import User, Employee, Document
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# ---- Field enums ----
STATUSES = (
    ('processing', 'In process'),
    ('denied', 'Denied'),
    ('negotiation', 'Negotiation'),
    ('opened', 'Opened'),
    ('closed', 'Closed'),
)

NEEDY_CATEGORIES = (
    ('large_families', 'Large Families'),
    ('low_income_families', 'Low Income Families'),
    ('retired_person', 'Retired Person'),
    ('single_parent_families', 'Single Parent Families'),
    ('orphan', 'Orphan'),
    ('refuge', 'Refuge'),
    ('person_without_a_fixed_residence_or_traveler_for_russians',
     'Person without a fixed residence or traveler for russians'),
    ('person_without_a_fixed_residence_or_traveler_for_foreign',
     'Person without a fixed residence or traveler for foreign'),
    ('debtor', 'debtor'),
    ('people_who_have_devoted_themselves_to_islam_or_for_study_of_the_Quran',
     'People who have devoted themselves to islam or for study of the Quran'),
    ('children_or_adults_with_disabilities_or_people_with_severe_diseases',
     'Children or adults with disabilities or people with severe diseases'),
)


# ---- Models ----

def send_request_notification():
    unread_requests = Request.objects.filter(status='processing').count() + Request.objects.filter(
        status='negotiation').count()
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'notification',
        {
            'type': 'notify',
            'requests': unread_requests
        })


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', null=True, blank=True)
    title = models.CharField(max_length=128)  # TODO: i18n
    description = models.TextField()  # TODO: i18n
    status = models.CharField(max_length=16, choices=STATUSES, default='processing')
    needy_category = models.CharField(max_length=70, choices=NEEDY_CATEGORIES, null=True, blank=True)
    goal = models.IntegerField(default=0)
    # documents = models.ArrayField(model_container=Document, default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    denying_reason = models.CharField(max_length=256, null=True, blank=True)  # TODO: i18n

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Request, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        send_request_notification()

    def delete(self, using=None, keep_parents=False):
        super(Request, self).delete(using=None, keep_parents=False)
        send_request_notification()


class Project(models.Model):
    created_by = models.ForeignKey(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)  # TODO: i18n
    description = models.TextField()  # TODO: i18n
    # property `campaigns` created with a backref
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Campaign(models.Model):
    request = models.OneToOneField(Request, on_delete=models.SET_NULL, null=True, blank=True,
                                   help_text='Either Request model will be created automatically')
    created_by = models.ForeignKey(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)  # TODO: i18n
    description = models.TextField()  # TODO: i18n
    goal = models.IntegerField()  # in rubles
    closing_reason = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='campaigns', blank=True,
                                help_text='Either Project model will be created automatically')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.request_id is None:
            request = Request.objects.create(title='Default title',
                                             description='Default description',
                                             goal=100)
            self.request = request

        if self.project_id is None:
            project = Project.objects.create(created_by=self.created_by,
                                             title='Default title',
                                             description='Default description')
            self.project = project

        super(Campaign, self).save(force_insert=force_insert,
                                   force_update=force_update,
                                   using=using,
                                   update_fields=update_fields)

    # property `transactions` created with a backref

    def get_status(self):
        return "Open" if self.closed_at is None else "Closed"

    def close_campaign(self, text_reason):
        if not text_reason:
            raise ValueError('In order to close campaign you nee to set som reason')
        self.closing_reason = text_reason
        self.closed_at = localtime()
        self.save()

    def get_payment_options(self):
        return self.payment_options.all()

    def payment_option_create(self, payment_option):
        payment_option.campaign = self
        payment_option.save()

    # TODO accomplish
    def get_collected_money(self):
        return 100

    # TODO accomplish
    def calculate_ratio(self):
        return self.get_collected_money() / self.goal

    def get_normal_date_view(self, date):
        try:
            return date.strftime("%Y %b %d")
        except:
            return None

    def get_normal_created_at_view(self):
        return self.get_normal_date_view(self.created_at)

    def get_normal_closed_at_view(self):
        return self.get_normal_date_view(self.closed_at)
