# Generated by Django 2.2.11 on 2020-03-14 12:00

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20200314_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('new', 'New'), ('processing', 'In process'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('campaigns', djongo.models.fields.ArrayField(default=[], model_container=projects.models.Campaign)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='accounts.Employee')),
            ],
        ),
    ]