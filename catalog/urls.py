from django.urls import path
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', GoodsListView.as_view(), name='products')
]