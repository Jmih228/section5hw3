from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def home(request):
    Products = Product.objects.all()
    context = {
        'object_list': Products,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)

def products(request):
    Products = Product.objects.all()
    context = {
        'object_list': Products,
        'title': 'Товары'
    }
    return render(request, 'catalog/products.html', context)

