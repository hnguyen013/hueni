"""
Tao file HTML xem truoc trang Chi tiet bai hoc (Task 3.3) bang du lieu Lesson
gia, KHONG can chay Django server, KHONG dung view/DB that.

Cach chay (dung tai thu muc co manage.py, da activate venv):
    python preview_lesson_detail.py

Se tao 2 file:
    lesson_preview_youtube.html  -> truong hop co video Youtube
    lesson_preview_no_video.html -> truong hop chua gan LessonVideo

Mo cac file nay bang trinh duyet de xem. Xong viec xoa di:
    Remove-Item preview_lesson_detail.py, lesson_preview_*.html
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from types import SimpleNamespace
from django.template.loader import render_to_string
from django.test import RequestFactory


class RelatedDoesNotExist:
    silent_variable_failure = True
    def __getattr__(self, item):
        raise AttributeError(item)


def make_lesson(title, slug, year_label, summary, cover_url, era_name, body="",
                 video_url="", video_file_url=""):
    lesson = SimpleNamespace(
        title=title, slug=slug, year_label=year_label, summary=summary,
        body=body,
        cover_image=SimpleNamespace(url=cover_url) if cover_url else None,
        era=SimpleNamespace(name=era_name),
    )
    if video_url or video_file_url:
        lesson.video = SimpleNamespace(
            title="", video_url=video_url,
            video_file=SimpleNamespace(url=video_file_url) if video_file_url else None,
        )
    else:
        lesson.video = RelatedDoesNotExist()
    return lesson


rf = RequestFactory()
request = rf.get("/bai-hoc/trong-dong-ngoc-lu/")

lesson_youtube = make_lesson(
    "Trống đồng Ngọc Lũ", "trong-dong-ngoc-lu", "~ 700 TCN",
    "Khám phá hoa văn và kỹ thuật đúc đồng cổ đại của người Việt xưa, một trong "
    "những hiện vật tiêu biểu nhất của văn hóa Đông Sơn.",
    "https://picsum.photos/seed/10/1200/600", "Thời kỳ Đông Sơn",
    body="Trống đồng Ngọc Lũ được phát hiện năm 1893 tại Hà Nam.\n\n"
         "Hoa văn trên mặt trống thể hiện đời sống sinh hoạt và tín ngưỡng của "
         "cư dân Đông Sơn cách đây hơn 2000 năm.",
    video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
)

lesson_no_video = make_lesson(
    "Kỹ thuật đúc đồng Đông Sơn", "ky-thuat-duc-dong", "~ 500 TCN",
    "Quy trình đúc đồng qua khuôn hai mảnh, một kỹ thuật tinh xảo của người xưa.",
    "https://picsum.photos/seed/11/1200/600", "Thời kỳ Đông Sơn",
    body="Nội dung bài học đang được biên soạn.",
)

for lesson, filename in [
    (lesson_youtube, "lesson_preview_youtube.html"),
    (lesson_no_video, "lesson_preview_no_video.html"),
]:
    html = render_to_string(
        "timeline/lesson_detail.html", {"lesson": lesson, "request": request}, request=request
    )
    html = html.replace("/static/dist/output.css", "static/dist/output.css")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Da tao {filename}")

print("Mo cac file .html vua tao bang trinh duyet de xem.")
