from django.shortcuts import render

# Create your views here.



def UserDashboard(request):
    return render(request,'pages/dashboard/dashboard.html')


def UserWallet(request):
    return render(request,'pages/dashboard/wallet.html')

def AffiliatePromotions(request):
    return render(request,'pages/dashboard/my-promotion.html')