from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Promotion(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='promotions')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_promotions')
    created=models.DateField(auto_now_add=True)
    views=models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.product.product_name}'