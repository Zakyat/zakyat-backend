from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='uploads')

    def get_absolute_url(self):
        return self.id
