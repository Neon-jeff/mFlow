"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='pages/home.html'),name='home'),
    path('auth/',include('authentication.urls')),
    path('dashboard/',include('creators.urls')),
    path('products/',include('products.urls')),
    path('affiliate-network/',TemplateView.as_view(template_name='pages/affiliate-network.html'),name='affiliate'),
    path('vendor-network/',TemplateView.as_view(template_name='pages/vendor-network.html'),name='vendor'),
    path('pricing/',TemplateView.as_view(template_name='pages/pricing.html'),name='pricing'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
