from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView
# Create your views here.

class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Главная'}

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class GoodsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    extra_context = {'title': 'Товары'}
