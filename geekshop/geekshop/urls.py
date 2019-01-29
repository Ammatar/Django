"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import mainapp.views as mainapp
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('', mainapp.products, name='index'),
    path('products/', mainapp.products, name='products'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('contact/', mainapp.contact, name='contact'),
    path('index1/', mainapp.index1, name='index1'),
    path('menu/', mainapp.menu, name='menu'),
    path('auth/', include(('authapp.urls', 'authapp'),namespace='auth')),
    path('basket/', include(('basketapp.urls', 'basketapp'), namespace='basket')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
