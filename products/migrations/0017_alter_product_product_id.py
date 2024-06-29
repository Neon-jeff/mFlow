# Generated by Django 4.2.3 on 2024-06-29 01:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('1ac10b44-4971-4830-bda6-22eec45a684e')),
        ),
    ]
