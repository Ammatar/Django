from django.contrib import admin
from authapp.models import ShopUser

# Register your models here.
from .models import ProductCategory, Product, Menu

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Menu)
admin.site.register(ShopUser)