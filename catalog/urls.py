from django.urls import path
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', GoodsListView.as_view(), name='products'),
    path('blog', BlogPostListView.as_view(), name='blog'),
    path('create_post/', BlogPostCreateView.as_view(), name='create'),
    path('edit/<int:pk>', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogPostDeleteView.as_view(), name='delete'),
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='view')
]
