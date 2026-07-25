"""
Filter dùng riêng cho section Video trong templates/timeline/lesson_detail.html
(Task 3.3). Admin có thể dán bất kỳ link Youtube dạng watch?v=... hoặc
youtu.be/... vào field LessonVideo.video_url (showcase/models.py) — filter
này chuyển nó thành dạng /embed/... để nhúng iframe được. Nếu không nhận
diện được (đã là link embed sẵn, hoặc là dịch vụ nhúng khác), trả về URL
gốc không đổi, không raise lỗi.
"""
from urllib.parse import urlparse, parse_qs

from django import template

register = template.Library()


@register.filter
def youtube_embed_url(url):
    if not url:
        return url

    parsed = urlparse(url)
    host = parsed.netloc.lower().replace('www.', '')

    if 'youtube.com' in host:
        if parsed.path.startswith('/embed/'):
            return url
        video_id = parse_qs(parsed.query).get('v', [None])[0]
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return url

    if host == 'youtu.be':
        video_id = parsed.path.lstrip('/')
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return url

    # Không phải link Youtube nhận diện được (Vimeo, link nhúng khác...) — giữ nguyên.
    return url
