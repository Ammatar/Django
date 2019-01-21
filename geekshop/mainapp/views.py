from django.shortcuts import render
from .models import Product, ProductCategory, Menu


menu_context = {'menu': Menu.objects.all()}
# Create your views here.
def main(request):
    title = 'главная'
    content = {'title': title}
    return render(request, 'mainapp/index.html', menu_context)


def products(request):
    return render(request, 'mainapp/products.html', menu_context, {'products': Product.objects.all()})


def contact(request):
    return render(request, 'mainapp/contact.html', menu_context)

def index1(request):
    return render(request, 'mainapp/index1.html', menu_context)

def menu (request):
    return render(request, 'mainapp/menu.html', menu_context)
