from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from uuid import uuid5
# Create your models here.

status=(
    ('closed','closed'),
    ('ongoing','ongoing')
)
class Promotion(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='promotions')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_promotions')
    created=models.DateField(auto_now_add=True)
    views=models.IntegerField()
    status=models.CharField(blank=True,null=True,choices=status,default='ongoing',max_length=50)
    promotion_link=models.UUIDField(null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.product.product_name} Affiliate Promotion'