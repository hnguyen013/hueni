from django.db import models

from timeline.models import Lesson


class LessonVideo(models.Model):
    """Video minh hoạ cho 1 bài học — hỗ trợ nhúng Youtube hoặc file tự upload."""

    lesson = models.OneToOneField(
        Lesson, on_delete=models.CASCADE, related_name='video'
    )
    title = models.CharField(max_length=255, blank=True)
    video_url = models.URLField(
        blank=True,
        help_text='Link Youtube (hoặc nhúng khác) — ưu tiên nếu có.',
    )
    video_file = models.FileField(
        upload_to='lessons/videos/', blank=True, null=True,
        help_text='Dùng nếu không có video_url (upload file video trực tiếp).',
    )

    class Meta:
        verbose_name = 'Lesson Video'
        verbose_name_plural = 'Lesson Videos'

    def __str__(self):
        return f'Video - {self.lesson.title}'


class Worksheet(models.Model):
    """Phiếu học tập đính kèm 1 bài học, có thể tải file về."""

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='worksheets'
    )
    title = models.CharField(max_length=255)
    preview_image = models.ImageField(
        upload_to='worksheets/previews/', blank=True, null=True
    )
    file = models.FileField(upload_to='worksheets/files/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Worksheet'
        verbose_name_plural = 'Worksheets'

    def __str__(self):
        return self.title


class QuizShowcase(models.Model):
    """Bộ câu hỏi (quiz) trưng bày dạng flashcard cho 1 bài học."""

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='quizzes'
    )
    title = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title or f'Quiz #{self.pk} - {self.lesson.title}'


class QuizQuestion(models.Model):
    """Một câu hỏi trong QuizShowcase, có nhiều QuizChoice."""

    quiz = models.ForeignKey(
        QuizShowcase, on_delete=models.CASCADE, related_name='questions'
    )
    question_text = models.TextField()
    explanation = models.TextField(
        blank=True, help_text='Giải thích hiện ra sau khi người dùng chọn đáp án.'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'

    def __str__(self):
        return self.question_text[:80]


class QuizChoice(models.Model):
    """Một lựa chọn trả lời của QuizQuestion."""

    question = models.ForeignKey(
        QuizQuestion, on_delete=models.CASCADE, related_name='choices'
    )
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Quiz Choice'
        verbose_name_plural = 'Quiz Choices'

    def __str__(self):
        return self.choice_text


class DigitalMap(models.Model):
    """Bản đồ số minh hoạ cho bài học — 3 kiểu: embed / image / geojson."""

    class MapType(models.TextChoices):
        EMBED = 'embed', 'Nhúng iframe'
        IMAGE = 'image', 'Ảnh tĩnh (lightbox)'
        GEOJSON = 'geojson', 'GeoJSON + Leaflet'

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='maps'
    )
    title = models.CharField(max_length=255, blank=True)
    map_type = models.CharField(
        max_length=20, choices=MapType.choices, default=MapType.EMBED
    )
    embed_url = models.URLField(
        blank=True, help_text="Dùng khi map_type = 'embed'."
    )
    image = models.ImageField(
        upload_to='maps/images/', blank=True, null=True,
        help_text="Dùng khi map_type = 'image'.",
    )
    geojson_file = models.FileField(
        upload_to='maps/geojson/', blank=True, null=True,
        help_text="Dùng khi map_type = 'geojson' (load bằng Leaflet.js).",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Digital Map'
        verbose_name_plural = 'Digital Maps'

    def __str__(self):
        return self.title or f'Map #{self.pk} - {self.lesson.title}'


class MapMarker(models.Model):
    """Một điểm đánh dấu (marker) trên DigitalMap kiểu geojson."""

    map = models.ForeignKey(
        DigitalMap, on_delete=models.CASCADE, related_name='markers'
    )
    label = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    note = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Map Marker'
        verbose_name_plural = 'Map Markers'

    def __str__(self):
        return self.label


class Gallery(models.Model):
    """Bộ hình ảnh (gallery) minh hoạ cho 1 bài học."""

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='galleries'
    )
    title = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title or f'Gallery #{self.pk} - {self.lesson.title}'


class GalleryImage(models.Model):
    """Một ảnh trong Gallery, có caption hiển thị trong lightbox."""

    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='galleries/images/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.caption or f'Image #{self.pk}'
