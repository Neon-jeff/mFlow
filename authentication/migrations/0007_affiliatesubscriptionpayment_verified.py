# Generated by Django 4.2.3 on 2024-06-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_affiliatesubscriptionpayment_proof_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliatesubscriptionpayment',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
