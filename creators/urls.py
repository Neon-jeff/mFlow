from django.urls import path
from .views import *

urlpatterns=[
    path('',UserDashboard,name='dashboard'),
    path('wallet/',UserWallet,name='wallet')
]
