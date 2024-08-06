import datetime

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        Payment.objects.all().delete()

        user1, created = User.objects.get_or_create(email='admin@sky.pro')

        course1, created = Course.objects.get_or_create(name='Test')
        course2, created = Course.objects.get_or_create(name='Test2')

        lesson1, created = Lesson.objects.get_or_create(name='Test3', course=course2)
        lesson2, created = Lesson.objects.get_or_create(name='Test3', course=course2)


        payment1 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            course=course1,
            amount=15000,
            payment_method='cash',
        )

        payment2 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            lesson=lesson1,
            amount=3000,
            payment_method='transfer to account',
        )

        payment3 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            lesson=lesson2,
            amount=5000,
            payment_method='transfer to account',
        )