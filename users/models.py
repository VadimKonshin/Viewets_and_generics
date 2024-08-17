from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course

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


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_pay = models.DateTimeField(verbose_name='дата оплаты', auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплата урока', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплата курса', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')])

    def __str__(self):
        return f'Платеж от {self.user} за {self.course}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Payments(models.Model):

    PAYMENT_METHOD = [('cash', 'наличные'),
                     ('online', 'перевод'),]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD)
    session_id = models.CharField(max_length=255, verbose_name='ID сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.user}, оплатил {self.course if self.course else self.lesson}, данную сумму {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
