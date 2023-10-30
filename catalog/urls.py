from django.urls import path
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', GoodsListView.as_view(), name='products'),
    path('create_post/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('blog', BlogPostListView.as_view(), name='blog'),
    path('create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path('edit/<int:pk>', BlogPostUpdateView.as_view(), name='edit_post'),
    path('delete/<int:pk>', BlogPostDeleteView.as_view(), name='delete_post'),
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='view_post')
]
