from django.urls import path
from .views import *

urlpatterns=[
    path('',UserDashboard,name='dashboard'),
    path('wallet/',UserWallet,name='wallet'),
    path('affiliate/my-promotions/',AffiliatePromotions,name='affiliate-promotions'),
    path('profile',AffiliateDetails,name='adetails'),
    path('subscription/',SelectSubscription,name='select-sub'),
    path('create-promotion/',CreatePromotion,name='create-promotion'),
    path('courses/',Courses,name='courses')

]
