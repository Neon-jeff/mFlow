# Generated by Django 4.2.3 on 2024-06-22 21:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='courses')),
                ('flyer', models.ImageField(blank=True, null=True, upload_to='flyers')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('4ddce661-e6b1-4371-8d4d-0a8b4eb33e89')),
        ),
    ]
