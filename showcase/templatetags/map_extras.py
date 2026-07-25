"""
Filter dùng riêng cho section Bản đồ số trong templates/showcase/_map.html
(Task 3.6). Leaflet.js (CDN) chỉ nên nhúng vào trang khi bài học thực sự có
ít nhất 1 DigitalMap kiểu 'geojson' — filter này kiểm tra điều đó trên
queryset/list map truyền vào, tránh Django template không có filter kiểu
"any()" dựng sẵn.
"""
from django import template

register = template.Library()


@register.filter
def has_geojson_map(map_list):
    if not map_list:
        return False
    return any(getattr(m, 'map_type', None) == 'geojson' for m in map_list)
