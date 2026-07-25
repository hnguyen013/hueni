from django.urls import path

from . import views

app_name = "timeline"

urlpatterns = [
    path("", views.TimelineHomeView.as_view(), name="home"),
    path("bai-hoc/<slug:slug>/", views.LessonDetailView.as_view(), name="lesson_detail"),
]
