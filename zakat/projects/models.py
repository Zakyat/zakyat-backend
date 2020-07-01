from djongo import models
from accounts.models import User, Employee


# ---- Field enums ----
STATUSES = (
    ('processing', 'In process'),
    ('denied', 'Denied'),
    ('negotiation', 'Negotiation'),
    ('opened', 'Opened'),
    ('closed', 'Closed'),
)

# TODO normal description of NEEDY_CATEGORIES
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

# TODO add fields + o2o --> FK + list of docs from accnts + add methods

class Request(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    status = models.CharField(max_length=16, choices=STATUSES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    # current should be aggregated from payments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='campaigns')
    # property `transactions` created with a backref

# TODO create table options

# TODO ? я не нашел все типы доков