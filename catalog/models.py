from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Превью', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    last_change_date = models.DateTimeField(verbose_name='Дата последнего изменения')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Blog_Post(models.Model):

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='post_previews/', verbose_name='Превью', null=True, blank=True)
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации')
    views_count = models.BigIntegerField(verbose_name='Количество просмотров')
