# Generated by Django 4.2.3 on 2024-06-14 00:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('21316a3c-8e73-41d2-92a5-cfdfc5638711')),
        ),
    ]
