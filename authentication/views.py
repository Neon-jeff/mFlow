from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest,JsonResponse
from .models import *
from .otp import CreateOtp
import json
from handlers.handlemails import SendOTPEmail
from django.contrib import messages
from .decorators import redirect_dashboard
# Create your views here.




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
    return render(request,'pages/login.html')
 
@login_required(login_url='login')
def EmailVerification(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.POST.get('otp')==profile.email_otp:
            profile.verified=True
            profile.save()
            return JsonResponse({"message":"OTP Verified"},safe=False)
        else:
            return HttpResponseBadRequest(content=json.dumps({"error":"Invalid OTP provided"}))
    return render(request,'pages/verify-email.html')