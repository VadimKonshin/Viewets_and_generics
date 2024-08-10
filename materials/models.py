from django.db import models

from config import settings


NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(verbose_name='Картинка', **NULLABLE, upload_to='materials/course_previews/')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец курса',
                              **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    preview = models.ImageField(verbose_name='Картинка', **NULLABLE, upload_to='materials/course_previews/')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на урок', **NULLABLE)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, verbose_name='курсы',
                               **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец уроков',
                              **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
