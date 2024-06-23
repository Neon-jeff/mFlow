from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
import uuid
from handlers.handlemails import SendSubEmail
# Create your models here.

ACCOUNT_TYPE_CHOICES=(
    ('affiliate','affiliate'),
    ('vendor','vendor'),
    ('Customer','Customer')
)
subscription_plans=(
    ('starter','starter'),
    ('pro','pro'),
    ('superior','superior')
)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    account_type=models.CharField(max_length=200,null=True,blank=True,choices=ACCOUNT_TYPE_CHOICES)
    email_verified=models.BooleanField(default=False,null=True,blank=True)
    profile_avatar=models.URLField(null=True,blank=True)
    sales_balance=models.PositiveIntegerField(default=0)
    withdrawal_address=models.CharField(max_length=50,null=True,blank=True)
    affiliate_balance=models.PositiveIntegerField(default=0)
    email_otp=models.CharField(null=True,blank=True,max_length=6)
    affiliate_link=models.UUIDField(unique=True,null=True,blank=True)
    onboarding_complete=models.BooleanField(default=False)

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
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='subscription')
    subscription_type=models.CharField(null=True,blank=True,max_length=100,choices=subscription_plans)
    created=models.DateField(auto_now_add=True)
    proof=models.ImageField(null=True,blank=True,upload_to='subscriptions')
    verified=models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} {self.subscription_type} Affiliate Subscription'
    
    def save(self,*args, **kwargs) -> None:
        old_instance=AffiliateSubscriptionPayment.objects.filter(id=self.id)
        if len(old_instance) != 0:
            if old_instance[0].verified !=self.verified and self.verified==True:
                SendSubEmail(self.user,self.subscription_type)
        return super(AffiliateSubscriptionPayment,self).save(*args, **kwargs)