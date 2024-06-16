from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Product
from uuid import uuid4,uuid5
from django.contrib import messages
import json
# Create your views here.

def UserProductsListView(request):
    return render(request,'pages/dashboard/products.html')

def SingleProductLink(request,pk):
    product=Product.objects.get(product_id=pk)
    return render(request,'pages/product-page.html',{"product":product})

def PromoteProduct(request):
    return render(request,'pages/dashboard/promote-products.html')


def CreateProduct(request):
    user:User=request.user
    products=Product.objects.filter(user=user)
    user_products=[{
        "name":product.product_name,
        "price":product.price,
        "location":product.location,
        "image":product.product_image.url,
        "type":product.product_type,
        "id":product.product_id
    } for product in products]
    if request.method=='POST':
        data=request.POST
        file=request.FILES
        Product.objects.create(
            user=user,
            product_name=data['product_name'],
            price=int(data['price']),
            product_type=data['product_type'],
            product_id=uuid5(uuid4(),user.email),
            product_image=file['image'],
        )
        messages.success(request,"Product Created")
        return JsonResponse({"status":"Successful"})
    return JsonResponse(list(user_products),safe=False)

def handle_payout():
    pass

def handles_promotions_earning():
    pass

def handles_subscription():
    pass