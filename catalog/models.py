from django.db import models

# Create your models here.
from django.db import models
from user.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Превью', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, default=14,  to_field='email', on_delete=models.CASCADE,
                             verbose_name='владелец')

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

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='post_previews/', verbose_name='Превью', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.BigIntegerField(default=0, verbose_name='Количество просмотров')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    version_title = models.CharField(max_length=150, verbose_name='Название')
    is_current_version = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return self.version_title

    @property
    def active_version(self):
        return Version.objects.filter(is_active=True, product_id=self.id).first()

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
