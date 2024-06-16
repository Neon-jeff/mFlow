from django.urls import path
from .views import *

urlpatterns=[
    path('user-products/',UserProductsListView,name='user-products'),
    path('create-product/',CreateProduct,name='create-product'),
    path('product-link/<str:pk>',SingleProductLink,name='product-link'),
    path('promote/',PromoteProduct,name='affiliate-market'),

]