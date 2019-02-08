from django.shortcuts import render
from .models import Product, ProductCategory, Menu
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


menu_context = {'menu': Menu.objects.all()}
# Create your views here.
def main(request):
    title = 'главная'
    content = {'title': title}
    return render(request, 'mainapp/index.html', menu_context)

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    return Product.objects.order_by("?").first()


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products

def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content, menu_context)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', content, menu_context)

def product(request, pk):
    _product = get_object_or_404(Product, pk=pk)
    return render(request, 'mainapp/product_detail.html', context={'product': _product})

def contact(request):
    return render(request, 'mainapp/contact.html', menu_context)

def index1(request):
    return render(request, 'mainapp/index1.html', menu_context)

def menu (request):
    return render(request, 'mainapp/menu.html', menu_context)

def login (request):
    return render(request,'authapp/login.html', menu_context)

def base(request):
    return render(request, 'mainapp/base.html')