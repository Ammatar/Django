from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')

def index1(request):
    return render(request, 'mainapp/index1.html')
