from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.decorators import check_onboarding
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