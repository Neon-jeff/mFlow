from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from authentication.decorators import check_onboarding
from django.contrib.auth.models import User
# Create your views here.

@check_onboarding
@login_required(login_url='login')
def UserDashboard(request):
    return render(request,'pages/dashboard/dashboard.html')


@login_required(login_url='login')
def UserWallet(request):
    return render(request,'pages/dashboard/wallet.html')


@login_required(login_url='login')
def AffiliatePromotions(request):
    return render(request,'pages/dashboard/my-promotion.html')


@login_required(login_url='login')
def SelectSubscription(request):
    return render(request,'pages/dashboard/subscription.html')

@login_required(login_url='login')
def VendorDetails(request):
    pass

@login_required(login_url='login')
def AffiliateDetails(request):
    user:User=request.user
    data={
        "first_name":user.first_name,
        "last_name":user.last_name,
        "email":user.email,
        "avatar":user.profile.profile_avatar,
        "sales_balance":user.profile.sales_balance,
        "affiliate_link":user.profile.affiliate_link,
        "account_type":user.profile.account_type,
        
    }
    return JsonResponse(data,safe=False)