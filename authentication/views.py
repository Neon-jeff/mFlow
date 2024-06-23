from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest,JsonResponse
from .models import *
from .otp import CreateOtp
import json
from handlers.handlemails import SendOTPEmail,SendResetPasswordEmail
from django.contrib import messages
from .decorators import redirect_dashboard
from uuid import uuid5,uuid4
from django.views.decorators.csrf import csrf_exempt# Create your views here.
from .models import AffiliateSubscriptionPayment
from django.core.exceptions import ObjectDoesNotExist



@redirect_dashboard
def RegisterView(request):
    if request.method=='POST':
        data=request.POST
        # check existing user
        if User.objects.filter(username=data['email']).exists():
            return HttpResponseBadRequest(content=json.dumps({"error":"user already exists"}))
        new_user=User.objects.create(first_name=data['first_name'],last_name=data['last_name'],username=data['email'],email=data['email'])
        new_user.set_password(data['password'])
        new_user.save()
        profile=Profile.objects.create(user=new_user,email_otp=CreateOtp())
        login(request,new_user) 
        SendOTPEmail(new_user,profile.email_otp)
        return JsonResponse({"message":"Registration Successful"},safe=False) 
    return render(request,'pages/register.html')

@redirect_dashboard
def LoginView(request):
    if request.method=='POST':
        data=request.POST
        user=authenticate(request,username=data['email'],password=data['password'])
        if user is None:
            return HttpResponseBadRequest(content=json.dumps({"error":"Invalid loin"}))
        login(request,user)
        return JsonResponse({"message":"Login Successful"},safe=False) 
    return render(request,'pages/login.html')
 
@login_required(login_url='login')
def EmailVerification(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.POST.get('otp')==profile.email_otp:
            profile.email_verified=True
            profile.save()
            return JsonResponse({"message":"OTP Verified"},safe=False)
        else:
            return HttpResponseBadRequest(content=json.dumps({"error":"Invalid OTP provided"}))
    return render(request,'pages/verify-email.html')

@csrf_exempt
@login_required(login_url='login')
def ChooseAccount(request):
    if request.method=='POST':
        account_type=request.POST['account_type']
        if account_type=='affiliate':
            request.user.profile.affiliate_link=uuid5(uuid4(),request.user.email)
        request.user.profile.account_type=account_type
        request.user.profile.onboarding_complete=True
        request.user.profile.save()
        return JsonResponse({"message":"Onboarding Complete"},safe=False)
    return render(request,'pages/choose.html')


@login_required(login_url='login')
def CreateSubscription(request):
    if request.method=='POST':
        image=request.FILES['image']
        data=request.POST
        AffiliateSubscriptionPayment.objects.create(
            user=request.user,
            subscription_type=data['bordered-radio'],
            proof=image
        )
        messages.success(request,'Subscription payment successful, wait for confirmation')
        return JsonResponse({"status":"success"},safe=False)
    return render(request,'pages/pay_subscription.html')


def SuscriptionSucess(request):
    return render(request,'pages/success.html')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')


def ForgotPasswordSendOtp(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            user.profile.email_otp=CreateOtp()
            user.profile.save()
            SendResetPasswordEmail(user,user.profile.email_otp)
            messages.success(request,'Password reset otp sent')
            return redirect(resolve_url('verify-identity') + f'?email={user.email}')
        except ObjectDoesNotExist:
            messages.error(request,'Account with email does not exist')
            return render(request,'pages/forgot-password.html')
    return render(request,'pages/forgot-password.html')

def VerifyIdentity(request):
    email=request.GET['email']
    user=User.objects.get(email=email)
    if request.method=='POST':
        if request.POST['otp']==user.profile.email_otp:
            messages.success(request,'Identity Verified,Update Your Password')
            return redirect(resolve_url('change-password') + f'?email={user.email}')
        else:
            messages.error(request,'Invalid OTP')
            return render(request,'pages/password-otp-confirm.html')
    return render(request,'pages/password-otp-confirm.html')

def ChangePassword(request):
    user=User.objects.get(email=request.GET['email'])
    if request.method=='POST':
        data=request.POST
        if data['password'] !=data['confirm']:
            messages.error(request,"Passwords do not match")
            return render(request,'pages/reset-password.html')
        else:
            user.set_password(data['password'])
            user.save()
            messages.success(request,'Password Updated')
            return redirect('login')
    return render(request,'pages/reset-password.html')

def test_uuid(request):
    user:User=request.user
    profile:Profile=Profile.objects.get(user=user)
    profile.affiliate_link=uuid5(uuid4(),user.email)
    profile.save()
    return JsonResponse({"status":"successful"},safe=False)