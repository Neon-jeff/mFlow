from django.urls import path
from .views import *

urlpatterns=[
    path('user-products/',UserProductsListView,name='user-products'),
    path('/product-link',)
]