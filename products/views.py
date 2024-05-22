from django.shortcuts import render

# Create your views here.

def UserProductsListView(request):
    return render(request,'pages/dashboard/products.html')