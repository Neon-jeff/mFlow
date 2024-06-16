from django.shortcuts import render

# Create your views here.

def UserProductsListView(request):
    return render(request,'pages/dashboard/products.html')

def SingleProductLink(request):
    return render(request,'pages/product-page.html')

def PromoteProduct(request):
    return render(request,'pages/dashboard/promote-products.html')


def handle_payout():
    pass

def handles_promotions_earning():
    pass

def handles_subscription():
    pass