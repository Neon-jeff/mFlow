# Generated by Django 4.2.3 on 2024-06-12 07:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('ce2230db-909b-4bcf-8b1d-c41800ed2a7f')),
        ),
    ]