# Generated by Django 2.2.13 on 2020-07-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20200709_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='projects.Campaign'),
        ),
    ]
