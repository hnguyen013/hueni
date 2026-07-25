from django.contrib import admin

from .models import (
    LessonVideo, Worksheet,
    QuizShowcase, QuizQuestion, QuizChoice,
    DigitalMap, MapMarker,
    Gallery, GalleryImage,
)


# ---------------------------------------------------------------------------
# Quiz: QuizShowcase -> QuizQuestion -> QuizChoice
# Django admin không hỗ trợ inline lồng 2 cấp (inline-trong-inline) theo mặc
# định, nên cách xử lý ở đây là:
#   - Trang QuizShowcase: nhập nhanh danh sách QuizQuestion (Tabular),
#     có "show_change_link" để bấm thẳng vào 1 câu hỏi.
#   - Trang QuizQuestion (đăng ký riêng): nhập QuizChoice (Tabular) đầy đủ.
# => Vẫn nhập được toàn bộ quiz chỉ trong 1-2 lần bấm, không cần rời khỏi
#    khu vực quiz.
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Digital Map: DigitalMap -> MapMarker (chỉ dùng khi map_type = 'geojson')
# ---------------------------------------------------------------------------

class MapMarkerInline(admin.TabularInline):
    model = MapMarker
    extra = 1
    fields = ('label', 'lat', 'lng', 'note', 'order')


@admin.register(DigitalMap)
class DigitalMapAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'map_type', 'order')
    list_filter = ('map_type', 'lesson')
    search_fields = ('title',)
    inlines = [MapMarkerInline]


# ---------------------------------------------------------------------------
# Gallery: Gallery -> GalleryImage
# ---------------------------------------------------------------------------

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ('image', 'caption', 'order')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order')
    list_filter = ('lesson',)
    search_fields = ('title',)
    inlines = [GalleryImageInline]


# ---------------------------------------------------------------------------
# LessonVideo & Worksheet: đăng ký độc lập để xem/lọc toàn bộ danh sách.
# Ngoài ra 2 model này (và DigitalMap) còn được nhúng StackedInline ngay
# trong trang Lesson (xem timeline/admin.py) để nhập nhanh trong 1 màn hình.
# ---------------------------------------------------------------------------

@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'title', 'video_url', 'video_file')
    search_fields = ('lesson__title', 'title')


@admin.register(Worksheet)
class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order')
    list_filter = ('lesson',)
    search_fields = ('title',)
