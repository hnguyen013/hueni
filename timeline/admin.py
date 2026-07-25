from django.contrib import admin

from .models import Era, Lesson
from showcase.models import LessonVideo, Worksheet, QuizShowcase, DigitalMap, Gallery


# ---------------------------------------------------------------------------
# Các khối nội dung trưng bày (showcase) được nhúng thẳng vào trang Lesson để
# nhập 1 bài học đầy đủ (video, phiếu, quiz, bản đồ, ảnh) trong 1 màn hình.
# - LessonVideo / Worksheet / DigitalMap: sửa trực tiếp tại đây (StackedInline).
# - QuizShowcase / Gallery: chỉ nhập nhanh title/order tại đây, bấm
#   "show_change_link" để vào đúng trang quản lý riêng (nơi có sẵn inline
#   QuizQuestion+QuizChoice / GalleryImage — xem showcase/admin.py).
# ---------------------------------------------------------------------------

class LessonVideoInline(admin.StackedInline):
    model = LessonVideo
    extra = 0
    max_num = 1
    fields = ('title', 'video_url', 'video_file')


class WorksheetInline(admin.StackedInline):
    model = Worksheet
    extra = 1
    fields = ('title', 'preview_image', 'file', 'order')


class DigitalMapInline(admin.StackedInline):
    model = DigitalMap
    extra = 0
    fields = ('title', 'map_type', 'embed_url', 'image', 'geojson_file', 'order')
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
    inlines = [
        LessonVideoInline,
        WorksheetInline,
        DigitalMapInline,
        QuizShowcaseInline,
        GalleryInline,
    ]
