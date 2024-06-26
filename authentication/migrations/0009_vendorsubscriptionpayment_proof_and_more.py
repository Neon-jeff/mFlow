# Generated by Django 4.2.3 on 2024-06-29 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0008_alter_affiliatesubscriptionpayment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorsubscriptionpayment',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='subscriptions'),
        ),
        migrations.AddField(
            model_name='vendorsubscriptionpayment',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vendorsubscriptionpayment',
            name='subscription_type',
            field=models.CharField(blank=True, choices=[('starter', 'starter'), ('pro', 'pro'), ('superior', 'superior')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendorsubscriptionpayment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
