# Generated by Django 4.2.3 on 2024-06-23 10:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('e26c13a4-218f-418c-9e4a-7078b4f0a625')),
        ),
    ]
