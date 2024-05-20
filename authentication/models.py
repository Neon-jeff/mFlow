from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ACCOUNT_TYPE_CHOICES=(
    ('Affiliate','Affiliate'),
    ('Creator','Creator'),
    ('Customer','Customer')
)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    account_type=models.CharField(max_length=200,null=True,blank=True,choices=ACCOUNT_TYPE_CHOICES)
    email_verified=models.BooleanField(default=False,null=True,blank=True)
    profile_avatar=models.URLField(null=True,blank=True)
    sales_balance=models.PositiveIntegerField(default=0)
    withdrawal_address=models.CharField(max_length=50,null=True,blank=True)