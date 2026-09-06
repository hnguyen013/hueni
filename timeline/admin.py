from django.contrib import admin

from .models import Era, Lesson
from showcase.models import LessonVideo, Worksheet, QuizShowcase, DigitalMap, Gallery


class LessonVideoInline(admin.StackedInline):
    model = LessonVideo
    extra = 0
    max_num = 1
    fields = ('title', 'video_url', 'video_file')


class WorksheetInline(admin.StackedInline):
    model = Worksheet
    extra = 1
    fields = ('title', 'preview_image_url', 'preview_image', 'file_url', 'file', 'order')


class DigitalMapInline(admin.StackedInline):
    model = DigitalMap
    extra = 0
    fields = ('title', 'map_type', 'embed_url', 'image_url', 'image', 'geojson_file', 'order')
    show_change_link = True


class QuizShowcaseInline(admin.TabularInline):
    model = QuizShowcase
    extra = 0
    fields = ('title', 'order')
    show_change_link = True


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0
    fields = ('title', 'order')
    show_change_link = True


@admin.register(Era)
class EraAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_label', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('order',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'era', 'year_label', 'order', 'is_published', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('order', 'is_published')
    list_filter = ('era', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary')
    ordering = ('order',)
    fieldsets = (
        (None, {
            'fields': (
                'era', 'title', 'slug', 'year_label', 'summary', 'body',
                'cover_image_url', 'cover_image',
                'order', 'is_published',
            ),
        }),
    )
    inlines = [
        LessonVideoInline,
        WorksheetInline,
        DigitalMapInline,
        QuizShowcaseInline,
        GalleryInline,
    ]
