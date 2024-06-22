# Generated by Django 4.2.3 on 2024-06-22 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('c372fef1-0d5c-47f7-aecc-be78fcacb5fa')),
        ),
    ]
