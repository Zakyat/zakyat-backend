from djongo import models
from accounts.models import User, Employee


# ---- Field enums ----
# TODO change statuses
STATUSES = (
    ('processing', 'In process'),
    ('denied', 'Denied'),
    ('negotiation', 'Negotiation'),
    ('opened', 'Opened'),
    ('closed', 'Closed'),
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