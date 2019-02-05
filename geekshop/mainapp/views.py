from django.shortcuts import render
from .models import Product, ProductCategory, Menu
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


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

def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content, menu_context)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
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