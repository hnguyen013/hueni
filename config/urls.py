"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve as serve_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timeline.urls')),
    path('showcase/', include('showcase.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    # Dev: static() lo cả static lẫn media, gọn như cũ (không đổi hành vi dev).
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif not getattr(settings, 'USE_S3_MEDIA', False):
    # Production, KHÔNG dùng S3: LƯU Ý — django.conf.urls.static.static()
    # tự trả về [] (no-op) khi DEBUG=False, đây là guard mặc định của
    # Django để tránh vô tình bật media serving ở production. Vì project
    # này không dùng CDN/S3 mặc định (xem DEPLOY.md mục 5/6), phải gọi
    # thẳng view django.views.static.serve để ảnh cover/worksheet/gallery
    # vẫn load được sau khi deploy — chấp nhận đánh đổi hiệu năng (Django
    # tự serve thay vì Nginx/S3) vì quy mô nhỏ của website trưng bày này.
    # Khi USE_S3_MEDIA=True, bỏ qua nhánh này vì ảnh đã phục vụ thẳng từ
    # domain S3 (MEDIA_URL trỏ ra ngoài, xem config/settings.py).
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve_static, {'document_root': settings.MEDIA_ROOT}),
    ]
