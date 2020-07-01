# Generated by Django 2.2.13 on 2020-07-01 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_paymentgathering'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progressing', 'in_processing'), ('distribution', 'in_the_process_of_distribution'), ('mny_in_th_gthr', 'money_in_the_gathering'), ('in_th_process_of_trnsf_mny', 'in_the_process_of_transferring_money'), ('mny_trnsf', 'money_transferred')], max_length=40)),
                ('gathering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camping_transaction', to='projects.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=20)),
                ('subscription_days', models.IntegerField(choices=[(None, 'Null'), (1, 'everyday'), (30, 'everymonth')])),
                ('type', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash'), ('transfer', 'Transfer'), ('withdraw', 'Withdraw')], max_length=16)),
                ('description', models.TextField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='projects.Campaign')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='paymentgathering',
            name='payment',
        ),
        migrations.AlterField(
            model_name='cardpaymentinfo',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_payment_infos', to='projects.Transaction'),
        ),
        migrations.AlterField(
            model_name='cashpaymentinfo',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_payment_infos', to='projects.Transaction'),
        ),
        migrations.DeleteModel(
            name='OtherPaymentInfo',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PaymentGathering',
        ),
        migrations.AddField(
            model_name='campaigntransaction',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camping_transaction', to='projects.Transaction'),
        ),
    ]
