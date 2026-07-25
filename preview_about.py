"""
Tao file HTML xem truoc trang Gioi thieu (Task 3.8) bang du lieu SiteContent/
TeamMember gia, KHONG can chay Django server, KHONG dung view/DB that.

Cach chay (dung tai thu muc co manage.py, da activate venv):
    python preview_about.py

Se tao file about_preview.html, mo bang trinh duyet de xem. Xong viec xoa:
    Remove-Item preview_about.py, about_preview.html
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from types import SimpleNamespace
from django.template.loader import render_to_string
from django.test import RequestFactory

hero = SimpleNamespace(
    title="Câu chuyện của chúng tôi",
    body="Kết nối quá khứ với tương lai thông qua không gian số. Chúng tôi tin rằng "
         "di sản không chỉ nằm trong bảo tàng, mà phải được sống và thở trong từng "
         "tương tác học tập của thế hệ mới.",
    image=SimpleNamespace(url="https://picsum.photos/seed/museum/1200/500"),
)
vision = SimpleNamespace(
    icon="visibility", title="Tầm nhìn",
    body="Trở thành nền tảng giáo dục số hàng đầu, nơi di sản văn hóa Việt Nam được "
         "tái hiện sống động, dễ dàng tiếp cận và truyền cảm hứng cho mọi thế hệ "
         "người học trên toàn cầu.",
)
mission = SimpleNamespace(
    icon="explore", title="Sứ mệnh",
    body="Xây dựng hệ sinh thái học liệu số chất lượng cao, kết hợp công nghệ hiện "
         "đại với chuyên môn học thuật sâu sắc, mang đến trải nghiệm khám phá lịch "
         "sử đa chiều và lôi cuốn.",
)
core_values = [
    SimpleNamespace(icon="verified", title="Tri thức chuẩn xác",
                     body="Nội dung được thẩm định kỹ lưỡng bởi các chuyên gia, đảm bảo "
                          "tính chính xác và giá trị học thuật cao nhất."),
    SimpleNamespace(icon="touch_app", title="Trải nghiệm tương tác",
                     body="Vượt ra khỏi trang sách truyền thống, mang đến không gian học "
                          "tập đa phương tiện, cho phép người dùng tự do khám phá."),
    SimpleNamespace(icon="lightbulb", title="Truyền cảm hứng",
                     body="Thiết kế kể chuyện bằng hình ảnh và công nghệ, khơi dậy niềm "
                          "đam mê tìm hiểu di sản văn hóa một cách tự nhiên."),
]
team_members = [
    SimpleNamespace(name="Nguyễn An", role="Giám đốc Nội dung",
                     avatar=SimpleNamespace(url="https://picsum.photos/seed/an/400/400")),
    SimpleNamespace(name="Trần Bình", role="Trưởng nhóm Kỹ thuật",
                     avatar=SimpleNamespace(url="https://picsum.photos/seed/binh/400/400")),
    SimpleNamespace(name="Lê Chi", role="Thiết kế Trải nghiệm",
                     avatar=SimpleNamespace(url="https://picsum.photos/seed/chi/400/400")),
    SimpleNamespace(name="Phạm Dũng", role="Cố vấn Học thuật",
                     avatar=SimpleNamespace(url="https://picsum.photos/seed/dung/400/400")),
]

rf = RequestFactory()
request = rf.get("/gioi-thieu/")
html = render_to_string(
    "pages/about.html",
    {"hero": hero, "vision": vision, "mission": mission,
     "core_values": core_values, "team_members": team_members, "request": request},
    request=request,
)
html = html.replace("/static/dist/output.css", "static/dist/output.css")

with open("about_preview.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Da tao about_preview.html — mo file nay bang trinh duyet de xem.")
