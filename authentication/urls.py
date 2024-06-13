from django.urls import path,include
from .views import *


urlpatterns=[
    path('login/',LoginView,name='login'),
    path('register/',RegisterView,name='register'),
    path('verify-email/',EmailVerification,name='verify-email')
]
