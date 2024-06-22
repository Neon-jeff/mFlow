# Generated by Django 4.2.3 on 2024-06-22 11:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_product_image_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('2054a067-dfad-4b77-a71a-864d68633d46')),
        ),
    ]