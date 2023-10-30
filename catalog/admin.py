from django.contrib import admin

from catalog.models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Blog_Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'creation_date', 'is_published', 'views_count')
    list_filter = ('views_count', 'is_published')
    search_fields = ('title', 'content')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_title', 'is_current_version')
    list_filter = ('product',)
    search_fields = ('product', 'version_title')
