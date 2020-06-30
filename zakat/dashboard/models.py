from django.db import models
from accounts.models import Employee
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Gatherings(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Gatherings, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

        layer = get_channel_layer()
        async_to_sync(layer.group_send)(
            'notification',
            {
                'type': 'notify',
                'gathering': Gatherings.objects.count()
            })
