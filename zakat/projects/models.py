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
    status = models.CharField(max_length=16, choices=STATUSES)
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
    closed_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
    
class Project(models.Model):
    created_by = models.OneToOneField(Employee, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)    # TODO: i18n
    description = models.TextField()    # TODO: i18n
    campaigns = models.ArrayField(Campaign, default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
