"""
Tao 1 file HTML xem truoc trang Timeline (Task 3.2) bang du lieu Era/Lesson gia,
KHONG can chay Django server, KHONG dung view/DB that.

Cach chay (dung tai thu muc co manage.py, da activate venv):
    python preview_timeline.py

Sau khi chay xong, mo file "timeline_preview.html" vua duoc tao bang trinh
duyet (double-click hoac keo tha vao Chrome/Edge/Firefox) de xem giao dien
that, day du font Google Fonts (can mang internet).

Xong viec co the xoa 2 file nay di:
    Remove-Item preview_timeline.py, timeline_preview.html
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from types import SimpleNamespace
from django.template.loader import render_to_string
from django.test import RequestFactory


class FakeQS(list):
    def all(self):
        return self


class FakeLesson:
    def __init__(self, title, slug, year_label, summary, cover_url):
        self.title = title
        self.slug = slug
        self.year_label = year_label
        self.summary = summary
        self.cover_image = SimpleNamespace(url=cover_url)

    def get_absolute_url(self):
        return f"/bai-hoc/{self.slug}/"


class FakeEra:
    def __init__(self, name, year_label, description, lessons):
        self.name = name
        self.year_label = year_label
        self.description = description
        self.lessons = FakeQS(lessons)


eras = [
    FakeEra(
        "Thời kỳ Đông Sơn", "700 TCN - 100 SCN",
        "Nền văn hóa đồ đồng rực rỡ với biểu tượng trống đồng.",
        [
            FakeLesson(
                "Trống đồng Ngọc Lũ", "trong-dong-ngoc-lu", "~ 700 TCN",
                "Khám phá hoa văn và kỹ thuật đúc đồng cổ đại của người Việt xưa.",
                "https://picsum.photos/seed/1/400/300",
            ),
            FakeLesson(
                "Kỹ thuật đúc đồng Đông Sơn", "ky-thuat-duc-dong", "~ 500 TCN",
                "Quy trình đúc đồng qua khuôn hai mảnh, một kỹ thuật tinh xảo.",
                "https://picsum.photos/seed/2/400/300",
            ),
        ],
    ),
    FakeEra(
        "Thời kỳ Lý - Trần", "1009 - 1400",
        "Giai đoạn phát triển rực rỡ của Phật giáo và kiến trúc hoàng cung.",
        [
            FakeLesson(
                "Hoàng thành Thăng Long", "hoang-thanh-thang-long", "Thế kỷ 11",
                "Kiến trúc cung điện qua các triều đại vẫn còn tồn tại tới ngày nay.",
                "https://picsum.photos/seed/3/400/300",
            ),
        ],
    ),
]

rf = RequestFactory()
request = rf.get("/")
html = render_to_string(
    "timeline/timeline_home.html", {"eras": eras, "request": request}, request=request
)

# Sua duong dan static tuong doi de mo truc tiep bang file:// khong can server.
html = html.replace("/static/dist/output.css", "static/dist/output.css")

with open("timeline_preview.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Da tao timeline_preview.html — mo file nay bang trinh duyet de xem.")
