# Generated by Django 2.2.13 on 2020-07-15 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='documents',
        ),
    ]
