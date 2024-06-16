# Generated by Django 4.2.3 on 2024-06-16 14:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_amount_in_stock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('7c4f5312-e986-40de-8163-9371ffd07861')),
        ),
    ]
