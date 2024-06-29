# Generated by Django 4.2.3 on 2024-06-28 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_4',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('eb31c303-00f2-48aa-8f3d-3e3329b2a117')),
        ),
    ]