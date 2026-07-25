"""
Task 5.1 — Fixture dữ liệu mẫu (demo data).

Tạo sẵn: 2 Era, 4 Lesson (mỗi lesson có đủ: 1 video, 1 worksheet, 1 quiz
3 câu hỏi, 1 bản đồ số, 1 gallery 4 ảnh) để nhóm test giao diện ngay,
không cần nhập tay qua /admin/.

Cách chạy:
    python manage.py seed_demo_data
    python manage.py seed_demo_data --reset   # xoá dữ liệu demo cũ rồi tạo lại

Ảnh dùng trong fixture là ảnh placeholder được sinh trực tiếp bằng Pillow
(không cần file ảnh thật kèm theo), video dùng link Youtube mẫu (phim mở,
được phép nhúng công khai), bản đồ dùng đủ cả 3 kiểu (embed/image/geojson)
xen kẽ giữa các bài học để test đủ nhánh giao diện Task 3.6.
"""
import io
import json

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction

from timeline.models import Era, Lesson
from showcase.models import (
    LessonVideo,
    Worksheet,
    QuizShowcase,
    QuizQuestion,
    QuizChoice,
    DigitalMap,
    MapMarker,
    Gallery,
    GalleryImage,
)

# Slug của toàn bộ Era demo — dùng để nhận diện & xoá khi chạy --reset.
DEMO_ERA_SLUGS = ['dung-nuoc', 'dai-viet']

# Video mẫu: phim mở (Creative Commons, được phép nhúng công khai), dùng
# chung cho cả 4 bài học demo — chỉ để test section Video, không liên quan
# nội dung lịch sử.
DEMO_VIDEO_URL = 'https://www.youtube.com/watch?v=aqz-KE-bpKQ'


def _placeholder_image(width, height, bg_color, label, fmt='JPEG'):
    """Sinh 1 ảnh placeholder đơn giản (nền màu + nhãn chữ) bằng Pillow,
    trả về django.core.files.base.ContentFile để gán thẳng vào ImageField."""
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=max(18, width // 22))
    except OSError:
        font = ImageFont.load_default()

    text_color = (255, 255, 255)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        ((width - text_w) / 2, (height - text_h) / 2 - bbox[1]),
        label, fill=text_color, font=font,
    )

    buffer = io.BytesIO()
    img.save(buffer, format=fmt, quality=85)
    buffer.seek(0)
    ext = 'jpg' if fmt == 'JPEG' else fmt.lower()
    filename = f"placeholder-{abs(hash(label)) % 100000}.{ext}"
    return ContentFile(buffer.read(), name=filename)


def _placeholder_worksheet_file(title):
    """Sinh 1 file .txt đơn giản làm nội dung phiếu học tập tải về (demo)."""
    content = (
        f"PHIẾU HỌC TẬP — {title}\n"
        "================================\n\n"
        "Đây là file demo dùng để test tính năng tải phiếu học tập.\n"
        "Vui lòng thay bằng file PDF/Word thật khi nhập liệu chính thức "
        "qua /admin/.\n"
    )
    return ContentFile(content.encode('utf-8'), name='phieu-hoc-tap-demo.txt')


def _placeholder_geojson():
    data = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {'name': 'Điểm demo'},
                'geometry': {'type': 'Point', 'coordinates': [105.8342, 21.0278]},
            }
        ],
    }
    return ContentFile(json.dumps(data, ensure_ascii=False).encode('utf-8'), name='demo.geojson')


# Bảng màu placeholder theo đúng token DESIGN.md (primary/secondary/tertiary...)
# để ảnh demo trông hài hoà với giao diện thay vì màu ngẫu nhiên.
PALETTE = [
    (0, 45, 55),      # primary
    (74, 101, 78),    # secondary
    (40, 40, 37),      # tertiary
    (61, 100, 112),    # surface-tint
]


class Command(BaseCommand):
    help = 'Tạo dữ liệu mẫu (2 Era, 4 Lesson kèm đủ video/worksheet/quiz/map/gallery) để test giao diện.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset', action='store_true',
            help='Xoá toàn bộ dữ liệu demo cũ (theo slug Era) trước khi tạo lại.',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options['reset']:
            deleted, _ = Era.objects.filter(slug__in=DEMO_ERA_SLUGS).delete()
            self.stdout.write(self.style.WARNING(f'Đã xoá {deleted} bản ghi demo cũ.'))

        eras_data = [
            {
                'slug': 'dung-nuoc',
                'name': 'Thời kỳ Dựng nước',
                'year_label': '2879 TCN – 208 TCN',
                'description': (
                    'Giai đoạn hình thành nhà nước đầu tiên của người Việt, '
                    'từ thời đại Hùng Vương đến nhà nước Âu Lạc.'
                ),
                'order': 1,
                'lessons': [
                    {
                        'slug': 'truyen-thuyet-con-rong-chau-tien',
                        'title': 'Truyền thuyết Con Rồng Cháu Tiên',
                        'year_label': '2879 TCN',
                        'summary': 'Câu chuyện khởi nguyên về nguồn gốc dân tộc Việt Nam.',
                        'map_type': DigitalMap.MapType.IMAGE,
                    },
                    {
                        'slug': 'thanh-co-loa',
                        'title': 'Thành Cổ Loa và kỹ thuật quân sự Âu Lạc',
                        'year_label': '257 TCN',
                        'summary': 'Kinh đô của nhà nước Âu Lạc với kiến trúc thành xoáy ốc độc đáo.',
                        'map_type': DigitalMap.MapType.GEOJSON,
                        'map_lat': 21.1044, 'map_lng': 105.8747,
                    },
                ],
            },
            {
                'slug': 'dai-viet',
                'name': 'Thời kỳ Đại Việt',
                'year_label': '938 – 1858',
                'description': (
                    'Giai đoạn độc lập tự chủ lâu dài, xây dựng nền văn hiến '
                    'và các triều đại phong kiến Việt Nam.'
                ),
                'order': 2,
                'lessons': [
                    {
                        'slug': 'chien-thang-bach-dang-938',
                        'title': 'Chiến thắng Bạch Đằng năm 938',
                        'year_label': '938',
                        'summary': 'Trận thủy chiến chấm dứt hơn 1000 năm Bắc thuộc.',
                        'map_type': DigitalMap.MapType.GEOJSON,
                        'map_lat': 20.9333, 'map_lng': 106.7833,
                    },
                    {
                        'slug': 'van-mieu-quoc-tu-giam',
                        'title': 'Văn Miếu – Quốc Tử Giám, biểu tượng khoa bảng',
                        'year_label': '1070',
                        'summary': 'Trường đại học đầu tiên của Việt Nam, biểu tượng của nền khoa bảng.',
                        'map_type': DigitalMap.MapType.EMBED,
                        'map_lat': 21.0293, 'map_lng': 105.8355,
                    },
                ],
            },
        ]

        lesson_order = 0
        for era_data in eras_data:
            lessons_data = era_data.pop('lessons')
            era, era_created = Era.objects.get_or_create(
                slug=era_data['slug'], defaults=era_data,
            )
            status = 'tạo mới' if era_created else 'đã có sẵn'
            self.stdout.write(f'Era "{era.name}" — {status}')

            for i, lesson_data in enumerate(lessons_data):
                lesson_order += 1
                map_type = lesson_data.pop('map_type')
                map_lat = lesson_data.pop('map_lat', 21.0278)
                map_lng = lesson_data.pop('map_lng', 105.8342)

                lesson, lesson_created = Lesson.objects.get_or_create(
                    slug=lesson_data['slug'],
                    defaults={
                        'era': era,
                        'title': lesson_data['title'],
                        'year_label': lesson_data['year_label'],
                        'summary': lesson_data['summary'],
                        'body': (
                            f"Đây là nội dung demo cho bài học \"{lesson_data['title']}\". "
                            'Nội dung chi tiết sẽ được biên soạn và nhập qua /admin/.'
                        ),
                        'order': lesson_order,
                        'is_published': True,
                    },
                )

                if not lesson_created:
                    self.stdout.write(f'  Lesson "{lesson.title}" — đã có sẵn, bỏ qua tạo nội dung con.')
                    continue

                color = PALETTE[lesson_order % len(PALETTE)]
                lesson.cover_image = _placeholder_image(1200, 800, color, lesson.title)
                lesson.save()

                # ---- Video ----
                LessonVideo.objects.create(
                    lesson=lesson,
                    title=f'Video giới thiệu — {lesson.title}',
                    video_url=DEMO_VIDEO_URL,
                )

                # ---- Worksheet ----
                worksheet = Worksheet.objects.create(
                    lesson=lesson,
                    title=f'Phiếu học tập — {lesson.title}',
                    order=1,
                )
                worksheet.preview_image = _placeholder_image(
                    800, 600, color, 'Phiếu học tập'
                )
                worksheet.file = _placeholder_worksheet_file(lesson.title)
                worksheet.save()

                # ---- Quiz (3 câu hỏi) ----
                quiz = QuizShowcase.objects.create(
                    lesson=lesson, title=f'Kiểm tra nhanh — {lesson.title}', order=1,
                )
                for q_index in range(1, 4):
                    question = QuizQuestion.objects.create(
                        quiz=quiz,
                        question_text=f'Câu hỏi demo số {q_index} về "{lesson.title}"?',
                        explanation=(
                            f'Đây là giải thích demo cho câu hỏi số {q_index} — '
                            'thay bằng nội dung thật khi nhập liệu qua /admin/.'
                        ),
                        order=q_index,
                    )
                    choices = [
                        (f'Đáp án đúng (demo {q_index})', True),
                        (f'Đáp án nhiễu A (demo {q_index})', False),
                        (f'Đáp án nhiễu B (demo {q_index})', False),
                        (f'Đáp án nhiễu C (demo {q_index})', False),
                    ]
                    for c_index, (choice_text, is_correct) in enumerate(choices, start=1):
                        QuizChoice.objects.create(
                            question=question, choice_text=choice_text,
                            is_correct=is_correct, order=c_index,
                        )

                # ---- Bản đồ số (xen kẽ 3 kiểu embed/image/geojson) ----
                digital_map = DigitalMap.objects.create(
                    lesson=lesson,
                    title=f'Bản đồ — {lesson.title}',
                    map_type=map_type,
                    order=1,
                )
                if map_type == DigitalMap.MapType.EMBED:
                    digital_map.embed_url = (
                        f'https://maps.google.com/maps?q={map_lat},{map_lng}&z=14&output=embed'
                    )
                elif map_type == DigitalMap.MapType.IMAGE:
                    digital_map.image = _placeholder_image(1200, 800, color, 'Bản đồ demo')
                elif map_type == DigitalMap.MapType.GEOJSON:
                    digital_map.geojson_file = _placeholder_geojson()
                digital_map.save()

                if map_type == DigitalMap.MapType.GEOJSON:
                    MapMarker.objects.create(
                        map=digital_map, label=lesson.title,
                        lat=map_lat, lng=map_lng,
                        note=f'Vị trí demo liên quan tới "{lesson.title}".', order=1,
                    )

                # ---- Gallery (4 ảnh) ----
                gallery = Gallery.objects.create(
                    lesson=lesson, title=f'Bộ hình ảnh — {lesson.title}', order=1,
                )
                for img_index in range(1, 5):
                    gallery_image = GalleryImage.objects.create(
                        gallery=gallery,
                        caption=f'Ảnh minh hoạ demo {img_index} — {lesson.title}',
                        order=img_index,
                    )
                    gallery_image.image = _placeholder_image(
                        900, 900, PALETTE[(lesson_order + img_index) % len(PALETTE)],
                        f'Ảnh {img_index}',
                    )
                    gallery_image.save()

                self.stdout.write(self.style.SUCCESS(f'  Lesson "{lesson.title}" — đã tạo đủ nội dung demo.'))

        self.stdout.write(self.style.SUCCESS(
            'Hoàn tất seed dữ liệu mẫu: 2 Era, 4 Lesson (video/worksheet/quiz/map/gallery).'
        ))
