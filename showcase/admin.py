from django.contrib import admin

from .models import (
    LessonVideo, Worksheet,
    QuizShowcase, QuizQuestion, QuizChoice,
    DigitalMap, MapMarker,
    Gallery, GalleryImage,
)


class QuizChoiceInline(admin.TabularInline):
    model = QuizChoice
    extra = 2
    fields = ('choice_text', 'is_correct', 'order')


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1
    fields = ('question_text', 'explanation', 'order')
    show_change_link = True


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'order')
    list_filter = ('quiz',)
    search_fields = ('question_text',)
    inlines = [QuizChoiceInline]


@admin.register(QuizShowcase)
class QuizShowcaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order')
    list_filter = ('lesson',)
    search_fields = ('title',)
    inlines = [QuizQuestionInline]


class MapMarkerInline(admin.TabularInline):
    model = MapMarker
    extra = 1
    fields = ('label', 'lat', 'lng', 'note', 'order')


@admin.register(DigitalMap)
class DigitalMapAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'map_type', 'order')
    list_filter = ('map_type', 'lesson')
    search_fields = ('title',)
    fields = ('lesson', 'title', 'map_type', 'embed_url', 'image_url', 'image', 'geojson_file', 'order')
    inlines = [MapMarkerInline]


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ('image_url', 'image', 'caption', 'order')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order')
    list_filter = ('lesson',)
    search_fields = ('title',)
    inlines = [GalleryImageInline]


@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'title', 'video_url', 'video_file')
    search_fields = ('lesson__title', 'title')


@admin.register(Worksheet)
class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order')
    list_filter = ('lesson',)
    search_fields = ('title',)
    fields = ('lesson', 'title', 'preview_image_url', 'preview_image', 'file_url', 'file', 'order')
