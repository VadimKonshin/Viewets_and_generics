from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    telephone = models.CharField(max_length=20, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(verbose_name='Аватар', **NULLABLE, upload_to='users/avatars')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользовватели'
