from django.shortcuts import render
from catalog.models import Product, Blog_Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
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


class BlogPostListView(ListView):
    model = Blog_Post
    extra_context = {'title': 'Блог'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = Blog_Post
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class BlogPostDetailView(DetailView):
    model = Blog_Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = Blog_Post
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:blog')
    template_name = 'catalog/blog_post_update_form.html'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = Blog_Post
    success_url = reverse_lazy('catalog:blog')
