from django.db import models
from django.contrib.auth.models import User
import uuid
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
    affiliate_balance=models.PositiveBigIntegerField(default=0)
    email_otp=models.PositiveBigIntegerField(null=True,blank=True)
    affiliate_link=models.UUIDField(unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} Profile'

class VendorSubscriptionPlan(models.Model):
    amount=models.PositiveIntegerField() 
    plan_name=models.CharField(max_length=100) 
    
    def __str__(self) -> str:
        return f'{self.plan_name} Affiliate Plan'

class AffiliateSubscriptionPlan(models.Model):
    amount=models.PositiveIntegerField() 
    plan_name=models.CharField(max_length=100) 
    
    def __str__(self) -> str:
        return f'{self.plan_name} Affiliate Plan'

class VendorSubscriptionPayment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    subscription_type=models.ForeignKey(VendorSubscriptionPlan,on_delete=models.PROTECT)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} {self.subscription_type.plan_name} Vendor Subscription'

class AffiliateSubscriptionPayment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    subscription_type=models.ForeignKey(AffiliateSubscriptionPlan,on_delete=models.PROTECT)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} {self.subscription_type.plan_name} Vendor Subscription'