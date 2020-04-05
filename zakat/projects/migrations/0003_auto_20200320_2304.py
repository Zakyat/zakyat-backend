# Generated by Django 2.2.11 on 2020-03-20 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200314_1526'),
        ('projects', '0002_auto_20200314_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='campaigns',
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='accounts.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='projects.Project')),
                ('request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Request')),
            ],
        ),
    ]
