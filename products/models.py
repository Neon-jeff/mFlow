from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

product_type=(
    ('ticket','ticket'),
    ('e-book','e-book'),
    ('physical','physical'),
    ('digial','digital')


)

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200,null=True,blank=True)
    price=models.PositiveIntegerField(null=True,blank=True)
    verified=models.BooleanField(default=False)
    views=models.PositiveIntegerField(default=0)
    product_type=models.CharField(max_length=200,null=True,blank=True,choices=product_type)
    location=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    product_id=models.UUIDField(default=uuid.uuid4())
    product_image=models.ImageField(upload_to='product_images',null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} Product'

