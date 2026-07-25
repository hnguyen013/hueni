# Tailwind CSS — Website Trưng bày Học liệu số

## Lựa chọn công cụ: Tailwind CLI (không dùng `django-tailwind`)

Lý do:
- Không cần tạo thêm 1 Django app phụ (`theme`) và không phải chạy song song 2
  tiến trình (`python manage.py tailwind start` + `runserver`).
- `tailwindcss` CLI là 1 gói npm dev-dependency duy nhất, build ra thẳng 1 file
  CSS tĩnh (`static/dist/output.css`) — Django chỉ cần serve như static file
  bình thường qua `{% load static %}`.
- Dễ tích hợp vào bước build khi deploy (Task 5.3): chỉ cần thêm
  `npm install && npm run build` vào build command trước khi
  `collectstatic`, không cần cài Node runtime lâu dài trên server production.

## Cấu trúc liên quan

```
tailwind.config.js       # design token: colors, fontFamily, borderRadius, spacing
package.json             # script build/watch
static/src/input.css     # entry point (@tailwind base/components/utilities)
static/dist/output.css   # file CSS đã build — dùng trong template
```

## Cài đặt (chỉ cần làm 1 lần)

```bash
npm install
```

## Build 1 lần (production / trước khi deploy)

```bash
npm run build
```

## Build tự động khi code (development)

```bash
npm run watch
```

## Dùng trong template Django

```html
{% load static %}
<link rel="stylesheet" href="{% static 'dist/output.css' %}">
```

## Design token đã cấu hình trong `tailwind.config.js`

| Token | Class Tailwind | Giá trị |
|---|---|---|
| Màu chính | `bg-primary` / `text-primary` | `#1a434e` |
| Màu phụ | `bg-secondary` / `text-secondary` | `#4a654e` |
| Nền trang | `bg-background` | `#f9f9f9` |
| Bề mặt card | `bg-surface-container-lowest` | `#ffffff` |
| Font tiêu đề | `font-heading` | Literata |
| Font nội dung | `font-sans` | Hanken Grotesk |
| Bo góc card | `rounded-xl` | `1.5rem` |
| Padding section | `py-section` (hoặc dùng class dựng sẵn `.section-padding`) | `8rem` |

Class dựng sẵn trong `static/src/input.css` (`@layer components`):
- `.card` — nền `surface-container-lowest`, `rounded-xl`, đổ bóng nhẹ.
- `.btn-pill` — nút pill màu `primary`, hover sang `secondary` (dùng cho nút "Bắt đầu" ở nav).
- `.section-padding` — padding dọc 8rem cho 1 section.

> Lưu ý: DESIGN.md gốc chưa được cung cấp đầy đủ khi thực hiện task này.
> Các giá trị màu/font/spacing ở trên lấy đúng theo mô tả trong task 1.2.
> Nếu DESIGN.md đầy đủ có thêm token khác (VD: các sắc độ surface container
> khác, error/warning color, spacing scale khác `section-padding`), hãy bổ
> sung trực tiếp vào `tailwind.config.js` rồi chạy lại `npm run build`.
