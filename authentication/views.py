from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.http import HttpResponseBadRequest,JsonResponse
from .models import *
from .otp import CreateOtp
import json
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
        Profile.objects.create(user=new_user,email_otp=CreateOtp())
        login(request,new_user) 
        return JsonResponse({"message":"Registration Successful"},safe=False) 
    return render(request,'pages/register.html')


def LoginView(request):
    return render(request,'pages/login.html')
 
