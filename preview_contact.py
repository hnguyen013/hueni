"""
Tao file HTML xem truoc trang Lien he (Task 3.9) bang du lieu gia,
KHONG can chay Django server, KHONG dung view/DB that.

Cach chay (dung tai thu muc co manage.py, da activate venv):
    python preview_contact.py

Se tao file contact_preview.html, mo bang trinh duyet de xem. Xong xoa:
    Remove-Item preview_contact.py, contact_preview.html
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from types import SimpleNamespace
from django.template.loader import render_to_string
from django.test import RequestFactory

contact_info = [
    SimpleNamespace(icon="mail", title="Email", body="hoc.lieu.so@vidu.vn"),
    SimpleNamespace(icon="call", title="Điện thoại", body="+84 24 1234 5678"),
    SimpleNamespace(icon="share", title="Mạng xã hội", body="facebook.com/hoclieuso"),
]

rf = RequestFactory()
request = rf.get("/lien-he/")
html = render_to_string(
    "pages/contact.html", {"contact_info": contact_info, "request": request}, request=request
)
html = html.replace("/static/dist/output.css", "static/dist/output.css")

with open("contact_preview.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Da tao contact_preview.html — mo file nay bang trinh duyet de xem.")
