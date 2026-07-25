from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("gioi-thieu/", views.about, name="about"),
    path("lien-he/", views.contact, name="contact"),
]
