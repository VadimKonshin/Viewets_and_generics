from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test23@mail.com')
        self.course = Course.objects.create(title='python', owner=self.user)
        self.lesson = Lesson.objects.create(title='django', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), self.lesson.title
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {'title': 'test',
                'video_url': 'https://www.youtube.com/123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {'title': 'test'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'test')

    def test_lesson_delete(self):
        url = reverse('materials:lesson_destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data,
            {'count': 1, 'next': None, 'previous': None, 'results':
                [{'id': self.lesson.pk, 'title': self.lesson.title, 'description': None,
                  'preview': None, 'video_url': None,
                  'course': self.lesson.course.pk, 'owner': self.lesson.owner.pk}]}
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test23@mail.com')
        self.course = Course.objects.create(title='python', owner=self.user)
        self.lesson = Lesson.objects.create(title='django', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

    def test_subscription(self):
        url = reverse("materials:subscription")
        data = {
            "course_id": self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('message'), 'Подписка удалена'
        )
