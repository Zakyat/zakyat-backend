# Generated by Django 2.2.13 on 2020-07-15 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200715_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='project',
            field=models.ForeignKey(blank=True, help_text='Either Project model will be created automatically', on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='request',
            field=models.OneToOneField(blank=True, help_text='Either Request model will be created automatically', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Request'),
        ),
    ]
