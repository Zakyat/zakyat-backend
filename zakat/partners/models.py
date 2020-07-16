from django.db import models
from django.urls import reverse


class Partner(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/')

    def get_absolute_url(self):
        return reverse('dashboard:partner:partner_detail', args=[self.id])
