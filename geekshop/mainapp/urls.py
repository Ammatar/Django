from django.urls import path
from django.conf.urls import url
from .views import products, product
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    url(r'^$', products, name='index'),
    url(r'^category/(?P<pk>\d+)/$', products, name='category'),
    url(r'^product/(?P<pk>\d+)/$', product, name='product'),
]