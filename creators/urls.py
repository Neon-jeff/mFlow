from django.urls import path
from .views import *

urlpatterns=[
    path('',UserDashboard,name='dashboard')
]
