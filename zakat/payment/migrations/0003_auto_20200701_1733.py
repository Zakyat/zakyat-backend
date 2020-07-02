# Generated by Django 2.2.13 on 2020-07-01 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_paymentoptions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_paymentoptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progressing', 'in_processing'), ('distribution', 'in_the_process_of_distribution'), ('mny_in_th_gthr', 'money_in_the_gathering'), ('in_th_process_of_trnsf_mny', 'in_the_process_of_transferring_money'), ('mny_trnsf', 'money_transferred')], max_length=40)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camping_transaction', to='projects.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CardPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rrn', models.CharField(max_length=20, unique=True)),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_payment_infos', to=settings.AUTH_USER_MODEL)),
                ('payment_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_payment_infos', to='projects.PaymentOptions')),
            ],
        ),
        migrations.CreateModel(
            name='CashPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_name', models.CharField(max_length=30)),
                ('payer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cash_payment_infos', to=settings.AUTH_USER_MODEL)),
                ('payment_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_payment_infos', to='projects.PaymentOptions')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='subscription_days',
            field=models.IntegerField(choices=[('null', 'NULL'), ('1', 'everyday'), ('30', 'everymonth')], default='NULL'),
        ),
        migrations.DeleteModel(
            name='PaymentOptions',
        ),
        migrations.AddField(
            model_name='cashpaymentinfo',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_payment_infos', to='payment.Transaction'),
        ),
        migrations.AddField(
            model_name='cardpaymentinfo',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_payment_infos', to='payment.Transaction'),
        ),
        migrations.AddField(
            model_name='campaigntransaction',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camping_transaction', to='payment.Transaction'),
        ),
    ]
