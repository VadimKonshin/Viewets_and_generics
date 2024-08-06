from django.contrib import admin

from materials.models import Lesson, Course


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'course', 'preview', 'description', 'video_url')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    inlines = [LessonInline]

    list_display = ('id', 'title', 'preview', 'description')
    list_filter = ('title',)
    search_fields = ('title',)