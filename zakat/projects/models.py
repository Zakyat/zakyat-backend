from djongo import models
from accounts.models import User, Employee


# ---- Field enums ----

STATUSES = (
    ('new',        'New'),
    ('processing', 'In process'),
    ('approved',   'Approved'),
    ('rejected',   'Rejected'),
)

# ---- Models ----

class Request(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    status = models.CharField(max_length=16, choices=STATUSES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    created_by = models.OneToOneField(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    # property `campaigns` created with a backref
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
