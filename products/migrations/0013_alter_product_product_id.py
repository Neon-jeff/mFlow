# Generated by Django 4.2.3 on 2024-06-23 00:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_course_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('b4790e26-2cc8-4dc6-9f89-024f0fa4d45b')),
        ),
    ]
