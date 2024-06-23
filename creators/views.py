from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from authentication.decorators import check_onboarding
from django.contrib.auth.models import User
from .models import Promotion
from products.models import Product,Course
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from uuid import uuid4,uuid5


# Create your views here.

@check_onboarding
@login_required(login_url='login')
def UserDashboard(request):
    user_promotions=[
        {
            **model_to_dict(promotion),
            'image':promotion.product.product_image.url,
            'name':promotion.product.product_name,
            'vendor':f'{promotion.product.user.first_name} {promotion.product.user.last_name}',
            'price':promotion.product.price
        }
        for promotion in Promotion.objects.filter(user=request.user)
    ]    
    return render(request,'pages/dashboard/dashboard.html',{'promotions':user_promotions})


@login_required(login_url='login')
def UserWallet(request):
    return render(request,'pages/dashboard/wallet.html')


@login_required(login_url='login')
def AffiliatePromotions(request):
    user_promotions=[
        {
            **model_to_dict(promotion),
            'image':promotion.product.product_image.url,
            'name':promotion.product.product_name,
            'vendor':f'{promotion.product.user.first_name} {promotion.product.user.last_name}',
            'price':promotion.product.price
        }
        for promotion in Promotion.objects.filter(user=request.user)
    ]
    return render(request,'pages/dashboard/my-promotion.html',{'promotions':user_promotions})


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
        "affiliate_balance":user.profile.affiliate_balance
    }
    return JsonResponse(data,safe=False)

@login_required(login_url='login')
@csrf_exempt
def CreatePromotion(request):
    if request.method=='POST':
        _data=request.POST
        product=Product.objects.get(product_id=_data['product'])
        promotion=Promotion.objects.create(
            user=request.user,
            product=product,
            views=0
        )
        promotion.promotion_link=uuid5(request.user.profile.affiliate_link,str(product.product_id))
        promotion.save()
        messages.success(request,'Product campaign created')
        return JsonResponse({"status":"success"},safe=False)
    

@login_required(login_url='login')
def Courses(request):
    courses=[
        {
            **model_to_dict(course),
            'file':course.file.url,
            'flyer':course.flyer.url

        }
        for course in Course.objects.all()

    ]
    return render(request,'pages/dashboard/courses.html',{'courses':courses})