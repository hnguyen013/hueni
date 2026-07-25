from django.db.models import Prefetch
from django.views.generic import DetailView, ListView

from .models import Era, Lesson


class TimelineHomeView(ListView):
    """
    Trang chủ / Hành trình — render templates/timeline/timeline_home.html.
    Template lặp `{% for era in eras %}` -> `{% for lesson in era.lessons.all %}`,
    nên context_object_name phải là 'eras', và lessons prefetch phải được lọc
    is_published=True ngay trong Prefetch để era.lessons.all() trong template
    trả về đúng danh sách đã lọc (không phải toàn bộ lessons).
    """

    model = Era
    template_name = "timeline/timeline_home.html"
    context_object_name = "eras"

    def get_queryset(self):
        return Era.objects.prefetch_related(
            Prefetch(
                "lessons",
                queryset=Lesson.objects.filter(is_published=True),
            )
        )


class LessonDetailView(DetailView):
    """
    Trang chi tiết bài học — render templates/timeline/lesson_detail.html.
    Template cần 1 object tên 'lesson' với:
      - lesson.era (select_related, dùng cho breadcrumb)
      - lesson.video (select_related, OneToOne ngược — Django hỗ trợ
        select_related trên reverse OneToOneField)
      - lesson.worksheets.all
      - lesson.quizzes.all -> .questions.all -> .choices.all
      - lesson.maps.all -> .markers.all
      - lesson.galleries.all -> .images.all
    Toàn bộ được nạp trong 1 query trọn gói (select_related + prefetch_related)
    để tránh N+1 khi template lặp qua từng section.
    """

    model = Lesson
    template_name = "timeline/lesson_detail.html"
    context_object_name = "lesson"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            Lesson.objects.filter(is_published=True)
            .select_related("era", "video")
            .prefetch_related(
                "worksheets",
                "quizzes__questions__choices",
                "maps__markers",
                "galleries__images",
            )
        )
