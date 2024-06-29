from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Product
from uuid import uuid4,uuid5
from django.contrib import messages
import json
from django.forms.models import model_to_dict
from creators.models import Promotion

# Create your views here.

def UserProductsListView(request):
    return render(request,'pages/dashboard/products.html')

def SingleProductLink(request,pk):
    product=Product.objects.get(product_id=pk)
    return render(request,'pages/product-page.html',{"product":product})

def PromoteProduct(request):
    user_promotions_ids=[promotion.product.id for promotion in Promotion.objects.filter(user=request.user)]
    print(user_promotions_ids)
    products=[
        {
            **model_to_dict(product),
            "product_image":product.product_image.url,
            "product_image_2":product.product_image_2.url,
            "product_image_3":product.product_image_3.url,
            "product_image_4":product.product_image_4.url,
            "user":f'{product.user.first_name} {product.user.last_name}',
            "in_user_campaign":True if product.id in user_promotions_ids else False,
            "promotions":len(product.promotions.all())
        } 
        for product in Product.objects.all().order_by('-id')]

        
    # all_products=list(Product.objects.values().order_by('-id'))
    return render(request,'pages/dashboard/promote-products.html',{'products':products})


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
            product_image=file['image1'],
            product_image_2=file['image2'],
            product_image_3=file['image3'],
            product_image_4=file['image4'],
            description=data['description']
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