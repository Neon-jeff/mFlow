# Generated by Django 4.2.3 on 2024-06-22 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0007_affiliatesubscriptionpayment_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliatesubscriptionpayment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
