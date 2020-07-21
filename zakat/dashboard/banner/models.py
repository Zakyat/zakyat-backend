from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='uploads')
