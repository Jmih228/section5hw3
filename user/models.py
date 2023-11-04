from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=15, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='страна')
    is_verificated = models.BooleanField(default=False, verbose_name='Подтверждение почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
