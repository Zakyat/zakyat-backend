from djongo import models
from accounts.models import User, Employee, Document

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
    ('person_without_a_fixed_residence_or_traveler_for_russians', 'Person without a fixed residence or traveler for russians'),
    ('person_without_a_fixed_residence_or_traveler_for_foreign', 'Person without a fixed residence or traveler for foreign'),
    ('debtor', 'debtor'),
    ('people_who_have_devoted_themselves_to_islam_or_for_study_of_the_Quran', 'People who have devoted themselves to islam or for study of the Quran'),
    ('children_or_adults_with_disabilities_or_people_with_severe_diseases', 'Children or adults with disabilities or people with severe diseases'),
)


# ---- Models ----

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', null=True, blank=True)
    title = models.CharField(max_length=128)  # TODO: i18n
    description = models.TextField()  # TODO: i18n
    status = models.CharField(max_length=16, choices=STATUSES, default='processing')
    needy_category = models.CharField(max_length=70, choices=NEEDY_CATEGORIES, null=True, blank=True)
    goal = models.IntegerField(default=0)
    documents = models.ArrayField(model_container=Document, default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    denying_reason = models.CharField(max_length=256, null=True, blank=True)  # TODO: i18n

class Project(models.Model):
    created_by = models.OneToOneField(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    # property `campaigns` created with a backref
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# TODO add fields
class Campaign(models.Model):
    request = models.OneToOneField(Request, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.OneToOneField(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    goal = models.IntegerField()        # in rubles
    closing_reason = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='campaigns')
    # property `transactions` created with a backref

    def get_status(self):
        return "Open" if self.closed_at is None else "Closed"